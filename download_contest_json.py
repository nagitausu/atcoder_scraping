import json
import pandas as pd
import urllib.request
import sys
import time

out_folder = "data/contests/"

contests = []
with open("data/contests/latest_20contests.csv", "r") as f:
    for line in f.readlines():
        contests.append(line.rstrip())

for contest in contests:
    print(contest)
    url = "https://atcoder.jp/contests/" + contest + "/standings/json"
    filename = out_folder + contest + ".json"
    urllib.request.urlretrieve(url, filename)
    time.sleep(3)
