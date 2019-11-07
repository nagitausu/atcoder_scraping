from urllib import request
import requests
from bs4 import BeautifulSoup
import csv
import time

MAX_PAGE_NUM = 327 

def parse_table(table):
    parsed = []
    rows = table.find_all("tr")
    for row in rows[1:]:
        parsed_row = []
        for cell_num, cell in enumerate(row.find_all(["td", "th"])):
            txt = cell.get_text().strip()
            parsed_row.append(txt)
        parsed.append(parsed_row)
    return parsed


if __name__ == "__main__":

    url = "https://codeforces.com/ratings/page/"

    # Create result-csv file
    filename = "data/rank.csv"
    with open(filename, "w") as f:
        f.write("rank,user,participation,rating\n")

    # Repeat page reloading and dump results
    for i in range(1, MAX_PAGE_NUM + 1):
        data = requests.get(url + str(i))
        soup = BeautifulSoup(data.text, "lxml")

        table = soup.find_all("table")[5]
        parsed = parse_table(table)
        print(parsed)
        
        with open(filename, "a", newline="") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(parsed)

        # Check content
        for line in parsed:
            print(" ".join([str(item) for item in line]))

        # Without this line, you may be arrested by Kanagawa police...
        time.sleep(1)