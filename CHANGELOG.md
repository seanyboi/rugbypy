<a name="1.0.0 (Data update)"></a>

# 1.0.0 (Data update) (2023-09-26)

### match

* Addition of `home_team` and `away_team` columns to `fetch_matches`.

### team

* Fixed a bug where `team_vs_id` was not showing the team id but the team name instead in `fetch_team_stats`.
* Addition of `players` column into `fetch_team_stats` so users can know what players played in a particular game.