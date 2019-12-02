# coding: utf-8
from collections import Counter
import json
import sys
import os
import glob
import pandas as pd
import csv

CONTEST_RESULT_JSON_PATH = "data/contest_results"
RANK_CSV = "data/latest_rank.csv"
TABLE_NAME = "data/latest_rating_table.csv"

result_files = glob.glob(CONTEST_RESULT_JSON_PATH + "/*")
result_files.sort()
contest_num = len(result_files)

rank = pd.read_csv(RANK_CSV)
contestants_num = len(rank)
rank.iloc[:, 0] = [r for r in range(contestants_num)]
rank.set_index("user", inplace=True)
user_dict = rank.to_dict("index")

time_rating_table = [[-1] * (contest_num + 1) for _ in range(contestants_num)]

date_list = [0] * (contest_num + 1)
date_list[0] = "~2016-07-16"

# Fill rating after contest
for i, result_file in enumerate(result_files):
    js = open(result_file, "r")
    data = json.load(js)

    date = data[0]["EndTime"].split("T")[0]
    date_list[i+1] = date
    print("Load:", i, date, result_file)

    for line in data:
        user = line["UserScreenName"]
        new_rating = line["NewRating"]
        if user in user_dict:
            user_id = user_dict[user]["rank"]
            time_rating_table[user_id][i+1] = new_rating

# Refer previous rating
for i in range(contestants_num):
    for j in range(contest_num):
        if time_rating_table[i][j] == -1:
            continue
        if time_rating_table[i][j+1] > 0:
            continue
        time_rating_table[i][j+1] = time_rating_table[i][j]


with open(TABLE_NAME, "w") as file:
    writer = csv.writer(file)
    writer.writerows(time_rating_table)
    print("Write:", TABLE_NAME)
