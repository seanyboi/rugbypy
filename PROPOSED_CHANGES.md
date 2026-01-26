# Proposed Changes to rugbypy

This document outlines the new features and enhancements made to the rugbypy library.

## Summary

This update introduces match-specific player statistics fetching capabilities, adds competition-level filtering across multiple functions. The changes enable users to retrieve comprehensive player statistics for entire matches using parallel processing, while also providing more flexible filtering options across all stat-fetching functions.

---

## New Features

### 1. New Function: `fetch_match_players_stats()` (match.py)

**Location:** `nbs/match.ipynb` → `rugbypy/match.py`

**Description:** Fetches player statistics for all players who participated in a specific match, supporting parallel processing for efficient data retrieval.

**Function Signature:**
```python
def fetch_match_players_stats(match_id: str, max_workers: int = 1) -> pd.DataFrame
```

**Parameters:**
- `match_id` (str): The unique identifier for the match
- `max_workers` (int): Number of parallel workers for fetching player stats (default: 1)

**Returns:**
- `pd.DataFrame`: Combined DataFrame with statistics for all players in the match, or empty DataFrame if no data available

**Key Features:**
- Automatically fetches player lists for both home and away teams
- Uses `ThreadPoolExecutor` for concurrent data fetching
- Handles errors gracefully for individual player fetch failures
- Combines all player statistics into a single DataFrame

**Implementation Details:**
- Internal helper function `get_list_of_players()` extracts unique player IDs from team statistics
- Uses `concurrent.futures` for parallel processing
- Integrates with existing `fetch_match_details()`, `fetch_team_stats()`, and `fetch_player_stats()` functions

---

## Enhanced Features

### 2. Enhanced Function: `fetch_player_stats()` (player.py)

**Location:** `nbs/player.ipynb` → `rugbypy/player.py`

**Description:** Significantly enhanced with `match_id` and `competition_id` filtering options, plus major code refactoring to eliminate duplication.

**Updated Function Signature:**
```python
def fetch_player_stats(
    player_id: str,
    date: typing.Optional[str] = None,
    match_id: typing.Optional[str] = None,        # NEW PARAMETER
    competition_id: typing.Optional[str] = None   # NEW PARAMETER
) -> pd.DataFrame
```

**New Parameters:**
- `match_id` (typing.Optional[str]): Filter by specific match identifier (default: None)
- `competition_id` (typing.Optional[str]): Filter by competition identifier (default: None)

**Behavior:**
- If `date` is provided: Filters by game date in YYYYMMDD format
- If `match_id` is provided: Filters by match ID (new)
- If `competition_id` is provided: Filters by competition (new)
- If none provided: Returns all player stats

**Code Improvements:**
- **Eliminated code duplication**: Data loading now happens once, then filters are applied conditionally
- **Better structure**: Separates data fetching from filtering logic
- **Enhanced docstring**: Complete documentation with all parameters

**Example Usage:**
```python
# Fetch stats for a specific match
player_stats = fetch_player_stats(
    player_id="24717f78",
    match_id="416f317e"
)

# Fetch stats for a specific competition
player_stats = fetch_player_stats(
    player_id="24717f78",
    competition_id="ee0c6883"
)
```

### 3. Enhanced Function: `fetch_team_stats()` (team.py)

**Location:** `nbs/team.ipynb` → `rugbypy/team.py`

**Description:** Enhanced with `match_id` filtering option and refactored for better code quality.

**Updated Function Signature:**
```python
def fetch_team_stats(
    team_id: str,
    date: typing.Optional[str] = None,
    match_id: typing.Optional[str] = None # NEW PARAMETER
) -> pd.DataFrame
```

**New Parameter:**
- `match_id` (typing.Optional[str]): Filter by match identifier (default: None)

**Code Improvements:**
- **Eliminated code duplication**: Data loading now happens once, then filters are applied
- **Enhanced docstring**: Complete documentation with all parameters
- **Fixed error message**: Now uses f-string with `{team_id}`

**Example Usage:**
```python
# Fetch stats for a specific competition
team_stats = fetch_team_stats(
    team_id="93542906",
    match_id="83a2de24"
)
```

---

## Technical Improvements

### 4. Documentation

- **Comprehensive docstrings** for all modified functions following consistent format
- **Clear parameter documentation** including types, descriptions, and defaults
- **Usage notes** about optional filter parameters
- **Documented helper functions** like `get_list_of_players()`

---

## Module Updates

The following modules have been updated with the new and enhanced functions:

1. **rugbypy/match.py** - Added `fetch_match_players_stats()` function
2. **rugbypy/player.py** - Enhanced `fetch_player_stats()` with `match_id` and `competition_id` parameters, refactored code structure
3. **rugbypy/team.py** - Enhanced `fetch_team_stats()` with `competition_id` parameter, refactored code structure, fixed error message
4. **rugbypy/_modidx.py** - Updated module index to include new function

---

## Usage Examples

### Fetching All Player Stats for a Match

```python
from rugbypy.match import fetch_match_players_stats

# Fetch all player stats for a specific match with parallel processing
match_stats = fetch_match_players_stats(
    match_id="416f317e",
    max_workers=4  # Use 4 parallel workers for faster fetching
)

print(match_stats.head())
```

### Fetching Individual Player Stats with Various Filters

```python
from rugbypy.player import fetch_player_stats

# Fetch all stats for a player
all_stats = fetch_player_stats(player_id="24717f78")

# Fetch stats for a specific match
match_stats = fetch_player_stats(
    player_id="24717f78",
    match_id="416f317e"
)

# Fetch stats for a specific date
date_stats = fetch_player_stats(
    player_id="24717f78",
    date="20250101"
)

# Fetch stats for a specific competition
competition_stats = fetch_player_stats(
    player_id="24717f78",
    competition_id="ee0c6883"
)

print(competition_stats)
```

### Fetching Team Stats with Various Filters

```python
from rugbypy.team import fetch_team_stats

# Fetch all stats for a team
all_stats = fetch_team_stats(team_id="93542906")

# Fetch stats for a specific match
match_stats = fetch_team_stats(
    team_id="93542906",
    match_id="83a2de24"
)

print(competition_stats)
```

---

## Breaking Changes

None. All changes are backward compatible. Existing code will continue to work without modifications.

---

## Dependencies

No new dependencies added. Uses existing libraries:
- `pandas`
- `concurrent.futures` (Python standard library)
- `typing` (Python standard library)

---

## Testing Recommendations

Before merging, consider testing:

### New Function Testing
1. `fetch_match_players_stats()` with various match IDs
2. `fetch_match_players_stats()` with different `max_workers` values (1, 2, 4, 8)
3. Performance comparison between serial (max_workers=1) and parallel execution

### Enhanced Function Testing
4. `fetch_player_stats()` with `match_id` parameter
5. `fetch_player_stats()` with `competition_id` parameter
6. `fetch_team_stats()` with `match_id` parameter
7. All three functions with `date` parameter (regression testing)
8. All functions with no optional parameters (regression testing)

### Error Handling Testing
9. Error handling when match, player, or team data is unavailable
10. Behavior when invalid IDs are provided
11. Edge cases with empty DataFrames

---

## Future Enhancements

Potential areas for future improvement:

### Validation & Safety
1. Add validation to ensure only one optional filter parameter is provided at a time
   - Currently, if multiple filters are passed, only the first in the if/elif chain is used
   - Consider raising `ValueError` when multiple filters are provided
2. Add input validation for date format (YYYYMMDD)

### Performance & Reliability
3. Add timeout parameter for individual player fetch operations
4. Add retry logic for failed player fetch requests
5. Add caching mechanism for frequently accessed matches
6. Add progress bar for long-running parallel operations
7. Support for filtering by multiple match IDs simultaneously

### Feature Enhancements
8. Add `season` filter parameter to player and team stat functions
9. Add date range filtering (start_date, end_date)
10. Add bulk fetching capabilities for multiple players/teams

---

## Author Notes

I wanted to adress the issue opened on the repository. I added a few enhancements in the meantime, as I am using the project on my side and I think this will facilitate the requesting (at least for me it does).
Let me know (lucas33220@gmail.com) if you have any idea of feature enhancement or new features I can implement in the future, I will gladly help. Thank you for the work and the data !

Lucas

**Date:** 2026-01-26
**Version:** 3.0.0 → 3.1.0 (proposed)
