"""
DS2500
Lainey Tsai
3/29/2026
Cleans the datasets as well as writes a new csv file to
share that makes analyzing win rates at home vs. away easier
"""

import csv

teams = [
    # Eastern Conference
    "ATL", "BOS", "BRK", "CHO", "CHI", "CLE", "DET",
    "IND", "MIA", "MIL", "NYK", "ORL", "PHI", "TOR", "WAS",

    # Western Conference
    "DAL", "DEN", "GSW", "HOU", "LAC", "LAL", "MEM",
    "MIN", "NOP", "OKC", "PHO", "POR", "SAC", "SAS", "UTA"
]

win = []
for team_name in teams:
    FILENAME = f"{team_name}_data.csv"
    with open(FILENAME, "r") as infile:
        teams_header = infile.readline().strip().split(",")
        headers = infile.readline().strip().split(",")
        score_headers = headers[:9]
        score_headers[3] = "Loc"
        score_headers[7] = "OppS"
        score_headers.insert(0, "Team")
        team_headers = headers[9:30]
        opponent_headers = headers[30:]

        all_games = {}
        for row in infile:
            temp_dct = {}
            score_dct = {}
            team_dct = {}
            opponent_dct = {}

            row = row.strip().split(",")

            # skips row if it doesn't contain data
            if row[0] == "Rk":
                continue

            score = row[:9]
            team = row[9:30]
            opponent = row[30:]


            # makes dct for score data (keys = score headers)
            score_dct[score_headers[0]] = team_name
            for i in range(len(score)):
                score_dct[score_headers[i+1]] = score[i]
            temp_dct["Score Data"] = score_dct

            game_num = score[1]
            if game_num == "":
                continue
            game_num = int(game_num) - 1


            # makes dct for team data (keys = team headers)
            for i in range(len(team_headers)):
                team_dct[team_headers[i]] = team[i]
            temp_dct["Team Data"] = team_dct


           # makes dct for opponent team data (keys = opponent headers)
            for i in range(len(opponent_headers)):
                opponent_dct[opponent_headers[i]] = opponent[i]
            temp_dct["Opponent Data"] = opponent_dct


            # game number as keys to access all game data (starts at 0)
            all_games[game_num] = temp_dct


        # calculates win rates
        home_win_count = 0
        home_loss_count = 0
        away_win_count = 0
        away_loss_count = 0
        for dct in range(len(all_games)):
            if all_games[dct]["Score Data"]["Loc"] == "@" and all_games[dct]["Score Data"]["Rslt"] == "L":
                away_loss_count += 1
            elif all_games[dct]["Score Data"]["Loc"] == "@" and all_games[dct]["Score Data"]["Rslt"] == "W":
                away_win_count += 1
            elif all_games[dct]["Score Data"]["Loc"] == "" and all_games[dct]["Score Data"]["Rslt"] == "L":
                home_loss_count += 1
            else:
                home_win_count += 1

        home_games = 0
        away_games = 0
        for game in all_games.values():
            if game["Score Data"]["Loc"] == "@":
                away_games += 1
            else:
                home_games += 1

        win.append([team_name, home_games, away_games, home_win_count, away_win_count, round(home_win_count / home_games, 4), round(away_win_count / away_games, 4)])

# writes a new file to look at win rates at home vs. away
header = ["team", "home_games", "away_games", "home_wins", "away_wins", "home_win_pct", "away_win_pct"]
with open("nba_win_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(win)