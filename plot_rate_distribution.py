# coding: utf-8
import matplotlib.pyplot as plt
import pandas as pd
import sys

BIN_WIDTH = 50
COLOR_CHANGE_TH = 400
MAX_RATE = 3800

rank = pd.read_csv(sys.argv[1])

ac_color_list = ["#808080",
                 "#804000",
                 "#008000",
                 "#00C0C0",
                 "#0000FF",
                 "#C0C000",
                 "#FF9000",
                 "#FF0000"]

cf_color_list = ["#808080",
                 "#008000",
                 "#03a89e",
                 "#0000FF",
                 "#aa00aa",
                 "#FF8C00",
                 "#FF8C00",
                 "#FF0000",
                 "#000000"]
cf_color_list += ["#FF0000"] * 10

fig = plt.figure(figsize=(10,7))

N, bins, patches = plt.hist(rank[rank["match"] >= 5]["rating"], \
                            bins= MAX_RATE // BIN_WIDTH, \
                            range=(0, MAX_RATE))

for i, p in enumerate(patches):
    if False:
        color = ac_color_list[i // (COLOR_CHANGE_TH // BIN_WIDTH)]
    else:
        rate = i * BIN_WIDTH
        if rate < 1200:
            color = cf_color_list[0]
        elif rate < 1400:
            color = cf_color_list[1]
        elif rate < 1600:
            color = cf_color_list[2]
        elif rate < 1900:
            color = cf_color_list[3]
        elif rate < 2100:
            color = cf_color_list[4]
        elif rate < 2200:
            color = cf_color_list[5]
        elif rate < 2400:
            color = cf_color_list[6]
        elif rate < 3000:
            color = cf_color_list[7]
        elif rate < 5000:
            color = cf_color_list[8]
    p.set_facecolor(color)
    p.set_alpha(0.7)
    p.set_edgecolor(color)

plt.xlim(0, MAX_RATE)
plt.ylim(0, 2400)
plt.xlabel("Rating", size=12)
plt.ylabel("Number of contestants", size=12)
plt.title("Codeforces Rating Distribution (active user, number of participations >= 5)")
plt.text(3370, 2430, "2019/11/08", size=12)
plt.tight_layout(True)
plt.show()
