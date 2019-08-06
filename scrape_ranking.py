from urllib import request
from bs4 import BeautifulSoup
import csv
import time

MAX_PAGE_NUM = 360

def parse_table(table):
    parsed = []
    rows = table.find_all("tr")
    for row in rows[1:]:
        parsed_row = []
        for cell_num, cell in enumerate(row.find_all(["td", "th"])):
            if cell_num == 1:
                for item_num, item in enumerate(cell.find_all("a")):
                    if item_num == 0:
                        parsed_row.append(item.attrs["href"][-2:])
                        continue
                    parsed_row.append(item.get_text())
                continue
            txt = cell.get_text().rstrip()
            parsed_row.append(txt)
        parsed.append(parsed_row)
    return parsed


if __name__ == "__main__":

    url = "https://atcoder.jp/ranking?page="

    # Create result-csv file
    filename = "data/rank.csv"
    with open(filename, "w") as f:
        f.write("rank,country,user,affiliation,birth,rating,highest,match,win\n")

    # Repeat page reloading and dump results
    for i in range(1, MAX_PAGE_NUM + 1):
        html = request.urlopen(url + str(i))
        soup = BeautifulSoup(html, "html.parser")

        table = soup.find_all("table", {"class":"table table-bordered table-striped th-center"})[0]
        parsed = parse_table(table)

        with open(filename, "a", newline="") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(parsed)

        # Check content
        for line in parsed:
            print(" ".join([str(item) for item in line]))

        # Without this line, you may be arrested by Kanagawa police...
        time.sleep(1)
