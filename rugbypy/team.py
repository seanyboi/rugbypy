# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/team.ipynb.

# %% auto 0
__all__ = ['fetch_team_stats']

# %% ../nbs/team.ipynb 4
import pandas as pd
import typing
import requests

# %% ../nbs/team.ipynb 5
def fetch_team_stats(team_id: str, date: typing.Optional[str] = None):
    """
    Fetches all team stats for a particular team or if a date is passed then just for a particular game
    """
    if date:
        print(f"Fetching team stats for team_id:{team_id} on date:{date}...")
    else:
        print(f"Fetching all team stats for team_id:{team_id}...")
    try:
        if date:
            team_url = f"https://github.com/seanyboi/rugbydata/blob/main/data/team/{team_id}/{date}.parquet?raw=true"
            team_stats = pd.read_parquet(team_url, engine="pyarrow")
            return team_stats
        else:
            team_url = (
                f"https://github.com/seanyboi/rugbydata/blob/main/data/team/{team_id}"
            )
            path = requests.get(team_url)
            urls = [
                f"https://github.com/seanyboi/rugbydata/blob/main/{p['path']}?raw=true"
                for p in path.json()["payload"]["tree"]["items"]
            ]
            team_stats = pd.concat((pd.read_parquet(u, engine="pyarrow") for u in urls))
            return team_stats
    except Exception as e:
        print(
            f"No team stats for {team_id} because the team id does not exist. Please raise an issue! - {e}"
        )
