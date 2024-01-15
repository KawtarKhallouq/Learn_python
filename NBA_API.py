from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import matplotlib.pyplot as plt
import pandas as pd
import requests

def one_dict(list_dict):
    keys = list_dict[0].keys()
    out_dict = {key: [] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

# Get NBA teams
nba_teams = teams.get_teams()

# Convert teams data to a DataFrame
dict_nba_team = one_dict(nba_teams)
df_teams = pd.DataFrame(dict_nba_team)

# Filter for the Golden State Warriors
df_warriors = df_teams[df_teams['nickname'] == 'Warriors']

# Get the team ID for the Warriors
id_warriors = df_warriors['id'].values[0]

# Request game data using the NBA API
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
games = gamefinder.get_data_frames()[0]

# Downloading data (optional, if not using the NBA API)
# filename = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"
# download(filename, "Golden_State.pkl")

# Read data from the pickle file (optional, if not using the NBA API)
# file_name = "Golden_State.pkl"
# games = pd.read_pickle(file_name)

# Filter games for Golden State Warriors home and away
games_home = games[games['MATCHUP'] == 'GSW vs. TOR']
games_away = games[games['MATCHUP'] == 'GSW @ TOR']

# Calculate and print the mean PLUS_MINUS for home and away games
print("Mean PLUS_MINUS for away games:", games_away['PLUS_MINUS'].mean())
print("Mean PLUS_MINUS for home games:", games_home['PLUS_MINUS'].mean())

# Plotting the PLUS_MINUS for home and away games
fig, ax = plt.subplots()
games_away.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)
games_home.plot(x='GAME_DATE', y='PLUS_MINUS', ax=ax)
ax.legend(["away", "home"])
plt.show()
