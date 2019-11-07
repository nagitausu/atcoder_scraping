# coding: utf-8
import matplotlib.pyplot as plt
import pandas as pd
import sys

BIN_WIDTH = 50
COLOR_CHANGE_TH = 400
MAX_RATE = 4200

rank = pd.read_csv(sys.argv[1])

color_list = ["#808080", "#804000", "#008000", "#00C0C0", "#0000FF", "#C0C000", "#FF9000", "#FF0000"]
color_list += ["#FF0000"] * 10

fig = plt.figure(figsize=(10,7))

N, bins, patches = plt.hist(rank[rank["match"] >= 5]["rating"], \
                            bins= MAX_RATE // BIN_WIDTH, \
                            range=(0, MAX_RATE))

for i, p in enumerate(patches):
    color = color_list[i // (COLOR_CHANGE_TH // BIN_WIDTH)]
    p.set_facecolor(color)
    p.set_alpha(0.7)
    p.set_edgecolor(color)

plt.xlim(0, MAX_RATE)
plt.ylim(0, 800)
plt.xlabel("Rate", size=12)
plt.ylabel("Number of contestants", size=12)
plt.title("AtCoder Rating Distribution (match >= 5)")
plt.text(3700, 810, "2019/11/08", size=12)
plt.tight_layout(True)
plt.show()
