import requests
from bs4 import BeautifulSoup
from app import create_app, db
from app.models import Standing
import unicodedata
import os
import time

def extract_points_table():
    url = "https://en.wikipedia.org/wiki/2024_Nepal_Premier_League"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    tables = soup.find_all("table", {"class": "wikitable"})

    target_table = None
    for table in tables:
        header_row = table.find("tr")
        headers = [th.text.strip() for th in header_row.find_all("th")]
        if headers[:8] == ['Pos', 'Team', 'Pld', 'W', 'L', 'NR', 'Pts', 'NRR']:
            target_table = table
            break

    if not target_table:
        print("Points table not found.")
        return

    rows = target_table.find_all("tr")[1:]  # Skip the header row
    points_table = []

    for row in rows:
        cols = row.find_all(["th", "td"])
        cols_text = [col.text.strip() for col in cols]
        if len(cols_text) >= 8:
            points_table.append(cols_text[:8])

    with create_app().app_context():
        db.session.query(Standing).delete()  # Clear existing data

        for team in points_table:
            nrr_value = unicodedata.normalize('NFKD', team[7])
            nrr = float(nrr_value.replace('−', '-'))
            new_team = Standing(
                pos=int(team[0]),
                team=team[1],
                pld=int(team[2]),
                w=int(team[3]),
                l=int(team[4]),
                nr=int(team[5]),
                pts=int(team[6]),
                nrr=nrr
            )
            db.session.add(new_team)

        db.session.commit()
        print("Database updated successfully!")

if __name__ == "__main__":
    extract_points_table()
