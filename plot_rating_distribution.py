# coding: utf-8
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

BIN_WIDTH = 50
COLOR_CHANGE_TH = 400
MAX_RATE = 3800
# Y_MAX = 0.05
Y_MAX = 2800

AC_COLOR_LIST = ["#808080",
                 "#804000",
                 "#008000",
                 "#00C0C0",
                 "#0000FF",
                 "#C0C000",
                 "#FF9000",
                 "#FF0000",
                 "#FF0000",
                 "#FF0000",
                 "#FF0000"]

CF_COLOR_LIST = ["#808080",
                 "#008000",
                 "#03a89e",
                 "#0000FF",
                 "#aa00aa",
                 "#FF8C00",
                 "#FF8C00",
                 "#FF0000",
                 "#000000"]

def plot_rating_distribution(a, name="AtCoder", freq=False, image_name=None, date_str=None):
    fig = plt.figure(figsize=(10,7))
    if freq:
        N, bins, patches = plt.hist(a, \
                                    bins= MAX_RATE // BIN_WIDTH, \
                                    range=(0, MAX_RATE), \
                                    weights=np.ones(len(a)) / float(len(a)))
    else:
        N, bins, patches = plt.hist(a, \
                                    bins= MAX_RATE // BIN_WIDTH, \
                                    range=(0, MAX_RATE))
    for i, p in enumerate(patches):
        if name == "AtCoder":
            color = AC_COLOR_LIST[i // (COLOR_CHANGE_TH // BIN_WIDTH)]
        elif name == "Codeforces":
            rate = i * BIN_WIDTH
            if rate < 1200:
                color = CF_COLOR_LIST[0]
            elif rate < 1400:
                color = CF_COLOR_LIST[1]
            elif rate < 1600:
                color = CF_COLOR_LIST[2]
            elif rate < 1900:
                color = CF_COLOR_LIST[3]
            elif rate < 2100:
                color = CF_COLOR_LIST[4]
            elif rate < 2200:
                color = CF_COLOR_LIST[5]
            elif rate < 2400:
                color = CF_COLOR_LIST[6]
            elif rate < 3000:
                color = CF_COLOR_LIST[7]
            else:
                color = CF_COLOR_LIST[8]
        else:
            print("Wrong contest name")
            exit()
        p.set_facecolor(color)
        p.set_alpha(0.7)
        p.set_edgecolor(color)

    plt.xlim(0, MAX_RATE)
    plt.ylim(0, Y_MAX)
    plt.xlabel("Rating", size=12)
    if freq:
        plt.ylabel("Freq per bin", size=12)
    else:
        plt.ylabel("Number of contestants per bin", size=12)
    plt.title("Codeforces Rating Distribution (active user, number of participations >= 5)")
    # plt.title("Rating Distribution")
    if date_str:
        plt.text(3400, Y_MAX + Y_MAX // 80, date_str, size=12)
    plt.tight_layout(True)
    if image_name:
        plt.savefig(image_name)
        plt.close()
    else:
        plt.show()

if __name__ == "__main__":
    rank = pd.read_csv(sys.argv[1])
    a = rank[rank["participation"] >= 5]["rating"].values
    print(rank[rank["participation"] >= 5]["rating"].describe())
    plot_rating_distribution(a, "Codeforces", date_str="2020/04/01")
