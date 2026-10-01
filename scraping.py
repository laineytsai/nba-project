"""
DS2500
Lainey Tsai
3/29/2026
Scrapes data from Basketball Reference website and saves each team's
data into separate CSV files
"""

import requests
from bs4 import BeautifulSoup
import csv

teams = [
    # Eastern Conference
    "ATL", "BOS", "BRK", "CHO", "CHI", "CLE", "DET",
    "IND", "MIA", "MIL", "NYK", "ORL", "PHI", "TOR", "WAS",

    # Western Conference
    "DAL", "DEN", "GSW", "HOU", "LAC", "LAL", "MEM",
    "MIN", "NOP", "OKC", "PHO", "POR", "SAC", "SAS", "UTA"
]

for team in teams:
    url = f"https://www.basketball-reference.com/teams/{team}/2024/gamelog/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")

    with open(f"{team}_data.csv", "w") as file:
        writer = csv.writer(file)

        for row in rows:
            cols = row.find_all(["td", "th"])
            data = [col.text.strip() for col in cols]
            writer.writerow(data)
