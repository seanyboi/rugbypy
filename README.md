rugbypy
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

`rugbypy` is a Python package that aims to make rugby data more
available to aid in the development of rugby analytics.

![PyPI - Downloads](https://img.shields.io/pypi/dm/rugbypy.png)

Data is updated daily 5AM UTC! Currently we only have data for 2022,
2023 & 2024

## Requirements

python version 3.9

## Install

``` sh
pip install rugbypy
```

## How to use

### Match Stats

You can fetch all the matches that occured on a particular date with:

``` python
from rugbypy.match import *
matches = fetch_matches(date="20230101")
matches
```

    Fetching matches on date: 20230101...

<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>match_id</th>
      <th>competition_id</th>
      <th>home_team_id</th>
      <th>home_team</th>
      <th>away_team_id</th>
      <th>away_team</th>
      <th>date</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>595735</td>
      <td>267979</td>
      <td>25907</td>
      <td>Northampton Saints</td>
      <td>25901</td>
      <td>Harlequins</td>
      <td>20230101</td>
    </tr>
    <tr>
      <th>1</th>
      <td>599464</td>
      <td>270557</td>
      <td>25965</td>
      <td>Cardiff Blues</td>
      <td>25968</td>
      <td>Ospreys</td>
      <td>20230101</td>
    </tr>
    <tr>
      <th>2</th>
      <td>599465</td>
      <td>270557</td>
      <td>25966</td>
      <td>Scarlets</td>
      <td>25967</td>
      <td>Dragons</td>
      <td>20230101</td>
    </tr>
    <tr>
      <th>3</th>
      <td>599466</td>
      <td>270557</td>
      <td>25926</td>
      <td>Ulster</td>
      <td>25925</td>
      <td>Munster</td>
      <td>20230101</td>
    </tr>
    <tr>
      <th>4</th>
      <td>599467</td>
      <td>270557</td>
      <td>25924</td>
      <td>Leinster</td>
      <td>25923</td>
      <td>Connacht</td>
      <td>20230101</td>
    </tr>
    <tr>
      <th>5</th>
      <td>597648</td>
      <td>270559</td>
      <td>25917</td>
      <td>Clermont Auvergne</td>
      <td>25922</td>
      <td>Stade Toulousain</td>
      <td>20230101</td>
    </tr>
  </tbody>
</table>
</div>

Then using that match id you can feed it into the match details
function:

``` python
from rugbypy.match import *
match_details = fetch_match_details(match_id="595735")
match_details
```

    Fetching match details for match_id:595735...

<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>match_id</th>
      <th>date</th>
      <th>season</th>
      <th>competition_id</th>
      <th>competition</th>
      <th>venue_id</th>
      <th>venue</th>
      <th>city_played</th>
      <th>home_team</th>
      <th>away_team</th>
      <th>home_team_id</th>
      <th>away_team_id</th>
      <th>completed</th>
      <th>is_tournament</th>
      <th>played_on_grass</th>
      <th>attendance</th>
      <th>home_team_form</th>
      <th>away_team_form</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>595735</td>
      <td>20230101</td>
      <td>2023</td>
      <td>267979</td>
      <td>Premiership Rugby</td>
      <td>26070</td>
      <td>cinch Stadium at Franklin's Gardens</td>
      <td>Northampton</td>
      <td>Northampton Saints</td>
      <td>Harlequins</td>
      <td>25907</td>
      <td>25901</td>
      <td>True</td>
      <td>True</td>
      <td>True</td>
      <td>None</td>
      <td>WLWWL</td>
      <td>WTLWL</td>
    </tr>
  </tbody>
</table>
</div>

### Team Stats

You can fetch the team stats for every game with:

``` python
from rugbypy.team import *
team_stats = fetch_team_stats(team_id="25901")
team_stats
```

    Fetching all team stats for team_id: 25901...

<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>team</th>
      <th>game_date</th>
      <th>team_id</th>
      <th>team_vs</th>
      <th>team_vs_id</th>
      <th>match_id</th>
      <th>players</th>
      <th>clean_breaks</th>
      <th>conversion_goals</th>
      <th>defenders_beaten</th>
      <th>...</th>
      <th>scrums_total</th>
      <th>scrums_won</th>
      <th>tackles</th>
      <th>territory</th>
      <th>total_free_kicks_conceded</th>
      <th>total_lineouts</th>
      <th>tries</th>
      <th>turnover_knock_on</th>
      <th>turnovers_conceded</th>
      <th>yellow_cards</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Harlequins</td>
      <td>20220102</td>
      <td>25901</td>
      <td>Gloucester Rugby</td>
      <td>25900</td>
      <td>593902</td>
      <td>[290946, 298485, 296815, 296184, 295534, 29512...</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>26.0</td>
      <td>...</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>94.0</td>
      <td>0.63</td>
      <td>1.0</td>
      <td>16.0</td>
      <td>2.0</td>
      <td>9.0</td>
      <td>15.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Harlequins</td>
      <td>20220108</td>
      <td>25901</td>
      <td>Exeter Chiefs</td>
      <td>116227</td>
      <td>593909</td>
      <td>[290946, 296815, 296184, 295534, 295121, 29484...</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>16.0</td>
      <td>...</td>
      <td>11.0</td>
      <td>9.0</td>
      <td>124.0</td>
      <td>0.55</td>
      <td>0.0</td>
      <td>10.0</td>
      <td>2.0</td>
      <td>8.0</td>
      <td>17.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Harlequins</td>
      <td>20220128</td>
      <td>25901</td>
      <td>Bath Rugby</td>
      <td>25898</td>
      <td>593913</td>
      <td>[158708, 299436, 298485, 296815, 296791, 29553...</td>
      <td>7.0</td>
      <td>1.0</td>
      <td>12.0</td>
      <td>...</td>
      <td>8.0</td>
      <td>7.0</td>
      <td>162.0</td>
      <td>0.50</td>
      <td>0.0</td>
      <td>9.0</td>
      <td>3.0</td>
      <td>11.0</td>
      <td>15.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Harlequins</td>
      <td>20220206</td>
      <td>25901</td>
      <td>Sale Sharks</td>
      <td>25908</td>
      <td>593922</td>
      <td>[158708, 299436, 299031, 298764, 298487, 29848...</td>
      <td>7.0</td>
      <td>2.0</td>
      <td>20.0</td>
      <td>...</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>71.0</td>
      <td>0.54</td>
      <td>2.0</td>
      <td>12.0</td>
      <td>2.0</td>
      <td>17.0</td>
      <td>26.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Harlequins</td>
      <td>20220213</td>
      <td>25901</td>
      <td>Saracens</td>
      <td>25909</td>
      <td>593929</td>
      <td>[158708, 299436, 298764, 298487, 298485, 29681...</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>23.0</td>
      <td>...</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>98.0</td>
      <td>0.56</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>1.0</td>
      <td>11.0</td>
      <td>17.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Harlequins</td>
      <td>20240421</td>
      <td>25901</td>
      <td>Sale Sharks</td>
      <td>25908</td>
      <td>597118</td>
      <td>[290946, 257545, 301432, 299436, 299031, 29681...</td>
      <td>8.0</td>
      <td>3.0</td>
      <td>36.0</td>
      <td>...</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>119.0</td>
      <td>0.45</td>
      <td>0.0</td>
      <td>21.0</td>
      <td>5.0</td>
      <td>8.0</td>
      <td>15.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Harlequins</td>
      <td>20240427</td>
      <td>25901</td>
      <td>Northampton Saints</td>
      <td>25907</td>
      <td>597122</td>
      <td>[290946, 257545, 301432, 300430, 299436, 29903...</td>
      <td>10.0</td>
      <td>4.0</td>
      <td>22.0</td>
      <td>...</td>
      <td>6.0</td>
      <td>5.0</td>
      <td>125.0</td>
      <td>0.45</td>
      <td>0.0</td>
      <td>12.0</td>
      <td>6.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Harlequins</td>
      <td>20240505</td>
      <td>25901</td>
      <td>Stade Toulousain</td>
      <td>25922</td>
      <td>597203</td>
      <td>[290946, 301432, 299436, 299031, 296815, 29679...</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>23.0</td>
      <td>...</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>92.0</td>
      <td>0.47</td>
      <td>0.0</td>
      <td>15.0</td>
      <td>4.0</td>
      <td>8.0</td>
      <td>16.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>59</th>
      <td>Harlequins</td>
      <td>20240511</td>
      <td>25901</td>
      <td>Exeter Chiefs</td>
      <td>116227</td>
      <td>597126</td>
      <td>[290946, 301432, 299436, 299031, 296815, 29679...</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>33.0</td>
      <td>...</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>133.0</td>
      <td>0.40</td>
      <td>0.0</td>
      <td>9.0</td>
      <td>4.0</td>
      <td>7.0</td>
      <td>11.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Harlequins</td>
      <td>20240518</td>
      <td>25901</td>
      <td>Bristol Rugby</td>
      <td>25899</td>
      <td>597132</td>
      <td>[290946, 301432, 299436, 299031, 299029, 29681...</td>
      <td>6.0</td>
      <td>4.0</td>
      <td>24.0</td>
      <td>...</td>
      <td>4.0</td>
      <td>3.0</td>
      <td>129.0</td>
      <td>0.45</td>
      <td>1.0</td>
      <td>16.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>12.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>61 rows × 42 columns</p>
</div>

You can then fetch the team stats for a particular team on a particular
date with:

``` python
from rugbypy.team import *
team_stats = fetch_team_stats(team_id="25901", date="20230108")
team_stats
```

    Fetching team stats for team_id: 25901 on date: 20230108...

<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>team</th>
      <th>game_date</th>
      <th>team_id</th>
      <th>team_vs</th>
      <th>team_vs_id</th>
      <th>match_id</th>
      <th>players</th>
      <th>clean_breaks</th>
      <th>conversion_goals</th>
      <th>defenders_beaten</th>
      <th>...</th>
      <th>scrums_total</th>
      <th>scrums_won</th>
      <th>tackles</th>
      <th>territory</th>
      <th>total_free_kicks_conceded</th>
      <th>total_lineouts</th>
      <th>tries</th>
      <th>turnover_knock_on</th>
      <th>turnovers_conceded</th>
      <th>yellow_cards</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>28</th>
      <td>Harlequins</td>
      <td>20230108</td>
      <td>25901</td>
      <td>Sale Sharks</td>
      <td>25908</td>
      <td>595741</td>
      <td>[158708, 299436, 299031, 298485, 295117, 29477...</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>24.0</td>
      <td>...</td>
      <td>7.0</td>
      <td>5.0</td>
      <td>125.0</td>
      <td>0.41</td>
      <td>0.0</td>
      <td>11.0</td>
      <td>2.0</td>
      <td>8.0</td>
      <td>17.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 42 columns</p>
</div>

### Player Stats

We have the ability to fetch player stats for all the games they have
been involved in. We firstly identify the \`player_id\`\` of a player by
searching our player manifest file.

``` python
from rugbypy.player import *
player_manifest = fetch_all_players()
player_manifest.head()
```

<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>player_id</th>
      <th>player_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>262799</td>
      <td>AJ MacGinty</td>
    </tr>
    <tr>
      <th>1</th>
      <td>295135</td>
      <td>Bevan Rodd</td>
    </tr>
    <tr>
      <th>2</th>
      <td>294815</td>
      <td>Tom Roebuck</td>
    </tr>
    <tr>
      <th>3</th>
      <td>294814</td>
      <td>Gus Warr</td>
    </tr>
    <tr>
      <th>4</th>
      <td>294810</td>
      <td>Sam Dugdale</td>
    </tr>
  </tbody>
</table>
</div>

Or we can search for a certain player through our similarity tool:

``` python
from rugbypy.player import *
individual_player = fetch_player(name="johnny sexton")
individual_player
```

<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>player_id</th>
      <th>player_name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1345</th>
      <td>16004</td>
      <td>Johnny Sexton</td>
    </tr>
    <tr>
      <th>2156</th>
      <td>291349</td>
      <td>Ayden Johnstone</td>
    </tr>
    <tr>
      <th>2795</th>
      <td>149315</td>
      <td>Anthony Watson</td>
    </tr>
  </tbody>
</table>
</div>

Once we have their `player_id` we can fetch their player stats using
[`fetch_player_stats`](https://seanyboi.github.io/rugbypy/player.html#fetch_player_stats).
In this example we fetch Johnny Sextons player stats:

``` python
from rugbypy.player import *
player_stats = fetch_player_stats(player_id="16004")
player_stats
```

    Fetching all player stats for player_id: 16004...

<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>player_id</th>
      <th>game_date</th>
      <th>name</th>
      <th>team</th>
      <th>team_id</th>
      <th>competition_id</th>
      <th>competition</th>
      <th>match_id</th>
      <th>team_vs</th>
      <th>team_vs_id</th>
      <th>...</th>
      <th>rucks_won</th>
      <th>runs</th>
      <th>tackles</th>
      <th>total_free_kicks_conceded</th>
      <th>total_lineouts</th>
      <th>tries</th>
      <th>try_assists</th>
      <th>turnover_knock_on</th>
      <th>turnovers_conceded</th>
      <th>yellow_cards</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>16004</td>
      <td>20220205</td>
      <td>Johnny Sexton</td>
      <td>Ireland</td>
      <td>3</td>
      <td>180659</td>
      <td>Six Nations</td>
      <td>595080</td>
      <td>Wales</td>
      <td>4</td>
      <td>...</td>
      <td>4.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>16004</td>
      <td>20220227</td>
      <td>Johnny Sexton</td>
      <td>Ireland</td>
      <td>3</td>
      <td>180659</td>
      <td>Six Nations</td>
      <td>595088</td>
      <td>Italy</td>
      <td>20</td>
      <td>...</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>16004</td>
      <td>20220312</td>
      <td>Johnny Sexton</td>
      <td>Ireland</td>
      <td>3</td>
      <td>180659</td>
      <td>Six Nations</td>
      <td>595091</td>
      <td>England</td>
      <td>1</td>
      <td>...</td>
      <td>4.0</td>
      <td>12.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>16004</td>
      <td>20220319</td>
      <td>Johnny Sexton</td>
      <td>Ireland</td>
      <td>3</td>
      <td>180659</td>
      <td>Six Nations</td>
      <td>595093</td>
      <td>Scotland</td>
      <td>2</td>
      <td>...</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>10.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>16004</td>
      <td>20220610</td>
      <td>Johnny Sexton</td>
      <td>Leinster</td>
      <td>25924</td>
      <td>270557</td>
      <td>United Rugby Championship</td>
      <td>594483</td>
      <td>Bulls</td>
      <td>25953</td>
      <td>...</td>
      <td>0.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>16004</td>
      <td>20221216</td>
      <td>Johnny Sexton</td>
      <td>Leinster</td>
      <td>25924</td>
      <td>271937</td>
      <td>European Rugby Champions Cup</td>
      <td>597405</td>
      <td>Gloucester Rugby</td>
      <td>25900</td>
      <td>...</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>16004</td>
      <td>20230204</td>
      <td>Johnny Sexton</td>
      <td>Ireland</td>
      <td>3</td>
      <td>180659</td>
      <td>Six Nations</td>
      <td>596205</td>
      <td>Wales</td>
      <td>4</td>
      <td>...</td>
      <td>3.0</td>
      <td>8.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>16004</td>
      <td>20230211</td>
      <td>Johnny Sexton</td>
      <td>Ireland</td>
      <td>3</td>
      <td>180659</td>
      <td>Six Nations</td>
      <td>596208</td>
      <td>France</td>
      <td>9</td>
      <td>...</td>
      <td>1.0</td>
      <td>5.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>16004</td>
      <td>20230312</td>
      <td>Johnny Sexton</td>
      <td>Ireland</td>
      <td>3</td>
      <td>180659</td>
      <td>Six Nations</td>
      <td>596216</td>
      <td>Scotland</td>
      <td>2</td>
      <td>...</td>
      <td>2.0</td>
      <td>5.0</td>
      <td>9.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>16004</td>
      <td>20230318</td>
      <td>Johnny Sexton</td>
      <td>Ireland</td>
      <td>3</td>
      <td>180659</td>
      <td>Six Nations</td>
      <td>596219</td>
      <td>England</td>
      <td>1</td>
      <td>...</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>16004</td>
      <td>20230909</td>
      <td>Johnny Sexton</td>
      <td>Ireland</td>
      <td>3</td>
      <td>164205</td>
      <td>Rugby World Cup</td>
      <td>596156</td>
      <td>Romania</td>
      <td>12</td>
      <td>...</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>4.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>16004</td>
      <td>20230916</td>
      <td>Johnny Sexton</td>
      <td>Ireland</td>
      <td>3</td>
      <td>164205</td>
      <td>Rugby World Cup</td>
      <td>596166</td>
      <td>Tonga</td>
      <td>16</td>
      <td>...</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>16004</td>
      <td>20230923</td>
      <td>Johnny Sexton</td>
      <td>Ireland</td>
      <td>3</td>
      <td>164205</td>
      <td>Rugby World Cup</td>
      <td>596175</td>
      <td>South Africa</td>
      <td>5</td>
      <td>...</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>11.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>16004</td>
      <td>20231007</td>
      <td>Johnny Sexton</td>
      <td>Ireland</td>
      <td>3</td>
      <td>164205</td>
      <td>Rugby World Cup</td>
      <td>596190</td>
      <td>Scotland</td>
      <td>2</td>
      <td>...</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>16004</td>
      <td>20231014</td>
      <td>Johnny Sexton</td>
      <td>Ireland</td>
      <td>3</td>
      <td>164205</td>
      <td>Rugby World Cup</td>
      <td>596195</td>
      <td>New Zealand</td>
      <td>8</td>
      <td>...</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>11.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>15 rows × 41 columns</p>
</div>

We can also fetch the player stats on a particular date using
[`fetch_player_stats`](https://seanyboi.github.io/rugbypy/player.html#fetch_player_stats).
In this example we fetch Johnny Sextons player stats on 2023-09-16:

``` python
from rugbypy.player import *
player_stats = fetch_player_stats(player_id="16004", date="20230916")
player_stats
```

    Fetching player stats for player_id: 16004 on date: 20230916...

<div>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>player_id</th>
      <th>game_date</th>
      <th>name</th>
      <th>team</th>
      <th>team_id</th>
      <th>competition_id</th>
      <th>competition</th>
      <th>match_id</th>
      <th>team_vs</th>
      <th>team_vs_id</th>
      <th>...</th>
      <th>rucks_won</th>
      <th>runs</th>
      <th>tackles</th>
      <th>total_free_kicks_conceded</th>
      <th>total_lineouts</th>
      <th>tries</th>
      <th>try_assists</th>
      <th>turnover_knock_on</th>
      <th>turnovers_conceded</th>
      <th>yellow_cards</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>11</th>
      <td>16004</td>
      <td>20230916</td>
      <td>Johnny Sexton</td>
      <td>Ireland</td>
      <td>3</td>
      <td>164205</td>
      <td>Rugby World Cup</td>
      <td>596166</td>
      <td>Tonga</td>
      <td>16</td>
      <td>...</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 41 columns</p>
</div>
