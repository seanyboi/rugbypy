<a name="2.0.0 Release"></a>

# 2.0.0 (Data update) (2025-01-06)

Since the last update Github have changed the way a user can fetch data from their website. Each user has a maximum of **60 requests per hour**, however, you can use your
Github API KEY to increase the number of requests and I shall be updating the repo soon to accomodate for this.

We are also pleased to announce that we have backfilled 2022, 2023 & 2024! :tada:

### player

The structure has changed to accomodate the above change, every player will now have an individual `{player_id}.parquet` file containing all of their player stats data that is updated daily.

- Fixed `fetch_player_stats` bug (5)[https://github.com/seanyboi/rugbypy/issues/5]
- Implementation of `compare_player_stats` requested (here)[https://github.com/seanyboi/rugbypy/pull/2/files]

### team

The structure has changed to accomodate the above change, every team will now have an individual `{team_id}.parquet` file containing all of their team stats data that is updated daily.

- Fixed `fetch_team_stats` bug (5)[https://github.com/seanyboi/rugbypy/issues/5]

<a name="1.0.0 (Data update)"></a>

# 1.0.0 (Data update) (2023-09-26)

### match

* Addition of `home_team` and `away_team` columns to `fetch_matches`.

### team

* Fixed a bug where `team_vs_id` was not showing the team id but the team name instead in `fetch_team_stats`.
* Addition of `players` column into `fetch_team_stats` so users can know what players played in a particular game.