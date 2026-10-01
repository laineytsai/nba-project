"""
DS2500
Lainey Tsai
3/31/2026
"""


def read_csv(filename):
    data = []
    with open(filename, "r") as infile:
        header = infile.readline().strip().split(",")
        for row in infile:
            line = row.strip().split(",")
            team = line[0]
            nums = [float(x) for x in line[1:]]
            new_row = [team] + nums
            data.append(new_row)

    return data, header

def find_avg_win_pct(data):
    win_pct_total = 0
    away_pct_total = 0
    count = 0
    for row in data:
        win_pct_total += row[5]
        away_pct_total += row[6]
        count += 1

    avg_home_pct = win_pct_total / count
    avg_away_pct = away_pct_total / count
    difference = avg_home_pct - avg_away_pct

    return avg_home_pct, avg_away_pct, difference

def compare_win_pct(data):
    home_count = 0
    away_count = 0
    for team in data:
        if team[5] > team[6]:
            print(f"{team[0]} {team[5]} > {team[6]}")
            home_count += 1
        else:
            away_count += 1
            print(f"{team[0]} {team[5]} < {team[6]}")

    return home_count, away_count


def main():
    data, header = read_csv("nba_win_data.csv")
    print(header)
    print(data)
    print("")

    avg_home_pct, avg_away_pct, difference = find_avg_win_pct(data)
    print(f"average win % at home: {round(avg_home_pct, 4)} \naverage win % away: {round(avg_away_pct, 4)}")
    print(f"{round(avg_home_pct, 4)} - {round(avg_away_pct, 4)} = {round(difference, 4)} \nis {round(difference, 4)} a meaningful difference?")
    print("that's around 8-9 more wins per 100 games when playing at home vs. away")
    print("")

    print("comparing win percentages at home vs. away")
    home_count, away_count = compare_win_pct(data)
    print(f"{home_count} teams played better at home, while {away_count} teams played better away")
    print(f"{round(home_count / (home_count + away_count), 4) * 100}% of teams benefited from playing on their home court")


main()


