<a name="3.0.0 Release"></a>

# 3.0.0 (Data update) (2026-01-04)

- Python 3.9 support deprecation, users must be on 3.11 or above to use this package

- Unique `rugbypy` ids for players, teams, competitions, matches & venues. For example: `3c394539` (Toulouse), `c01ff111` (Jac Morgan)

- New leagues added

- New stats added:
    - team
        - `22m_entries` - 22 metre entries
        - `22m_conversion` - 22 metre conversion rate
        - `line_breaks` - line breaks made
        - `post_contact_metres` - metres gained after contact
        - `dominant_tackles` - dominant tackles made
        - `tackle_turnover` - tackles resulting in turnovers
        - `tackle_offload_allowed` - tackles where offload was allowed
        - `ruck_speed_0_3_pct` - percentage of rucks completed in 0-3 seconds
        - `ruck_speed_3_6_pct` - percentage of rucks completed in 3-6 seconds
        - `ruck_speed_6_plus_pct` - percentage of rucks completed in 6+ seconds
        - `team_vs_score` - opponent's score
        - `players` - list of player IDs in the match
    - player
        - `position` - updated playing position (e.g., `blindside_flanker`, `prop`)
        - `tackles_completed` - successful tackles
        - `dominant_tackles` - dominant tackles made
        - `ruck_turnovers` - turnovers won at the ruck
        - `carries_per_minute` - carries per minute played
        - `total_tackles_per_minute` - tackles per minute played
    - match
        - `venue_id` - unique venue identifier
        - `competition_id` - unique competition identifier

- New data added:
    - `competition` - competition registry with unique IDs
    - `venue` - venue registry with unique IDs
    - `match` - match registry with unique IDs


### player

The structure has changed to accomodate the above change, every player will now have an individual `{player_id}.parquet` file containing all of their player stats data that is updated daily.

- Fixed `fetch_player_stats` bug (5)[https://github.com/seanyboi/rugbypy/issues/5]
- Implementation of `compare_player_stats` requested (here)[https://github.com/seanyboi/rugbypy/pull/2/files]

### team

The structure has changed to accomodate the above change, every team will now have an individual `{team_id}.parquet` file containing all of their team stats data that is updated daily.

- Fixed `fetch_team_stats` bug (5)[https://github.com/seanyboi/rugbypy/issues/5]

<a name="2.0.0 Release"></a>

# 2.0.0 (Data update) (2025-01-06)

- Python 3.8 support deprecation

- Since the last update Github have changed the way a user can fetch data from their website. Each user has a maximum of **60 requests per hour**, however, you can use your
Github API KEY to increase the number of requests and I shall be updating the repo soon to accomodate for this.

- We are also pleased to announce that we have backfilled 2022, 2023 & 2024! :tada:

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