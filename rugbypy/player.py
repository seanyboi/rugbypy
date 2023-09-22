# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/player.ipynb.

# %% auto 0
__all__ = ['fetch_all_players', 'fetch_player', 'fetch_player_stats']

# %% ../nbs/player.ipynb 4
import pandas as pd
import requests
import typing
from collections import Counter
from math import sqrt

# %% ../nbs/player.ipynb 5
def fetch_all_players():
    """Fetches all players in the rugbypy manifest file."""
    try:
        player_manifest_url = f"https://github.com/seanyboi/rugbydata/blob/main/data/player/player_manifest.parquet?raw=true"
        players = pd.read_parquet(player_manifest_url, engine="pyarrow")
        return players
    except Exception as e:
        print(f"No player manifest exists. Please raise an issue! - {e}")

# %% ../nbs/player.ipynb 6
def word2vec(word):
    # Count the number of characters in each word.
    count_characters = Counter(word)

    # Gets the set of characters and calculates the "length" of the vector.
    set_characters = set(count_characters)

    length = sqrt(sum(c * c for c in count_characters.values()))

    return count_characters, set_characters, length, word

# %% ../nbs/player.ipynb 7
def cosine_similarity(vector1, vector2, ndigits):
    # Get the common characters between the two character sets
    common_characters = vector1[1].intersection(vector2[1])

    # Sum of the product of each intersection character.
    product_summation = sum(
        vector1[0][character] * vector2[0][character] for character in common_characters
    )

    # Gets the length of each vector from the word2vec output.
    length = vector1[2] * vector2[2]

    # Calculates cosine similarity and rounds the value to ndigits decimal places.
    if length == 0:
        # Set value to 0 if word is empty.
        similarity = 0
    else:
        similarity = round(product_summation / length, ndigits)

    return similarity

# %% ../nbs/player.ipynb 8
def fetch_player(
    name: str,  # the name of the rugby player you wish to fetch the id for.
):
    """Uses a similarity tool to fetch a players id"""
    players = fetch_all_players()
    all_players = players["player_name"].to_list()
    # Initiate an empty list to store results.
    results_list = []

    # Apply word2vec function to each name and store them in a list.
    vector_list = [word2vec(str(i)) for i in all_players]
    vector_name = word2vec(str(name))
    # Two loops to compare each vector with another vector only once.
    for i in range(len(vector_list)):
        # Get first vector
        vector1 = vector_list[i]

        # Calculate cosine similarity
        similarity_score = cosine_similarity(vector1, vector_name, 3)

        # Append to results list if similarity score is between 1 and the threshold.
        # Note that scores of 1 can be ignored here if we want to exclude people with the same name.
        if 1 >= similarity_score >= 0.75:
            results_list.append([vector1[3], vector_name[3], similarity_score])

        else:
            pass
    # Convert list to dataframe.
    results_df = pd.DataFrame(results_list)
    if len(results_df) != 0:
        results_df.columns = ["player_name", "comparison_name", "similarity_score"]
        results_df = results_df.sort_values(
            by="similarity_score", ascending=False
        ).head(3)
        player_id = players.loc[
            players["player_name"].isin(results_df["player_name"].to_list())
        ]
        return player_id
    else:
        # Can add error here if there's no results to return if desired.
        print(
            f"Apologies, we could not find a match for {name}. Please try again or raise an issue!"
        )

# %% ../nbs/player.ipynb 10
def fetch_player_stats(
    player_id: str,  # the player id of a particular player.
    date: typing.Optional[
        str
    ] = None,  # the date of a particular match you wish to fetch the player stats for.
):
    """
    Fetches all player stats for a particular player or if a date is passed then just for a particular game.
    """
    if date:
        print(f"Fetching player stats for player_id:{player_id} on date:{date}...")
    else:
        print(f"Fetching all player stats for player_id:{player_id}...")
    try:
        if date:
            player_url = f"https://github.com/seanyboi/rugbydata/blob/main/data/player/{player_id}/{date}"
            path = requests.get(player_url)
            urls = [
                f"https://github.com/seanyboi/rugbydata/blob/main/{p['path']}?raw=true"
                for p in path.json()["payload"]["tree"]["items"]
            ]
            player_stats = pd.concat(
                (pd.read_parquet(u, engine="pyarrow") for u in urls)
            )
            return player_stats
        else:
            player_url = f"https://github.com/seanyboi/rugbydata/blob/main/data/player/{player_id}"
            path = requests.get(player_url)
            date_urls = [
                f"https://github.com/seanyboi/rugbydata/blob/main/{p['path']}"
                for p in path.json()["payload"]["tree"]["items"]
            ]
            player_urls = [requests.get(url) for url in date_urls]
            player_urls = [
                p.json()["payload"]["tree"]["items"][0]["path"] for p in player_urls
            ]
            player_stats_url = [
                f"https://github.com/seanyboi/rugbydata/blob/main/{p}?raw=true"
                for p in player_urls
            ]
            player_stats = pd.concat(
                (pd.read_parquet(u, engine="pyarrow") for u in player_stats_url)
            )
            return player_stats
    except Exception as e:
        print(
            f"No player stats for {player_id} because the player id does not exist. Please raise an issue! - {e}"
        )
