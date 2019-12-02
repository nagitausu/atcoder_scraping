import os
import json
import pandas as pd
import urllib.request
import time

CONTESTS_JSON = "data/latest_contests.json"
RESULT_PATH = "data/contest_results/"

contests = pd.read_json(CONTESTS_JSON)
contests.sort_values("start_epoch_second", ascending=True, inplace=True)
rated_contests = contests[contests["rate_change"] != "-"]

for index, row in rated_contests.iterrows():
    contest_epoch = row["start_epoch_second"]
    contest_id = row["id"]
    filename = RESULT_PATH + str(contest_epoch) + "_" + str(contest_id) + ".json"
    if os.path.exists(filename):
        print("Skip:", filename)
    else:
        url = "https://atcoder.jp/contests/" + contest_id + "/results/json"
        print("Download:", url)
        urllib.request.urlretrieve(url, filename)
        print("Saved:", filename)
        time.sleep(3)
