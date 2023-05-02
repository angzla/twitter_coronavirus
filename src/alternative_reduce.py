#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths', nargs='+', required=True)
parser.add_argument('--keys', nargs='+', required=True)
args = parser.parse_args()
print(args.keys)

# imports
import json
from collections import Counter, defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

for key in args.keys:
    sorted(args.input_paths)
    yaxis = []
    total = defaultdict(lambda: Counter())
    errors = 0
    for path in args.input_paths:
        with open(path) as f:
            temp = json.load(f)
            number = 0
            try:
                for k in temp[key]:
                    number += temp[key][k]
            except KeyError:
                pass
            yaxis.append(number)
    plt.plot(np.arange(732), yaxis, label=key)
plt.ylabel('Number of Tweets')
months = ["Jan.", "March", "May", "July", "Sept.", "Nov."]
dates = [0, 58, 119, 180, 242, 303]
plt.xticks(dates, months)
plt.xlabel('Date')
plt.title("Hashtags used in Tweets per Day in 2020")
plt.legend()
plt.tight_layout()
plt.savefig('alternative')
