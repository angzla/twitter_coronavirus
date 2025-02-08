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
print("import json done")
from collections import Counter, defaultdict
print("import collections done")
import matplotlib
print("matplotlib done")
matplotlib.use('Agg')
import matplotlib.pyplot as plt
print("matplotlib.pyplot")
import numpy as np
print("numpy done")
print("imports done")
for key in args.keys:
    sorted(args.input_paths)
    yaxis = [0] * 366
    total = defaultdict(lambda: Counter())
    errors = 0
for path in args.input_paths:
    with open(path) as f:
        temp = json.load(f)
        try:
            for k, v in temp[key].items():
                if k.isdigit():
                    day = int(k)  # Ensure `k` is a valid day index
                    if 0 <= day < 366:
                        yaxis[day] += v  # Aggregate tweets per day
        except KeyError:
            pass


#for path in args.input_paths:
 #       with open(path) as f:
  #          temp = json.load(f)
   #         number = 0
    #        try:
     #           for k in temp[key]:
      #              number += temp[key][k]
       #     except KeyError:
        #        pass
         #   yaxis.append(number)
plt.plot(np.arange(366), yaxis, label=key)
plt.ylabel('Number of Tweets')
months = ["Jan.", "Feb.", "March", "April", "May", "June"]
dates = [0, 31, 60, 91, 121, 152]  # Approximate month start days in 2020
plt.xticks(dates, months)
plt.xlabel('Date')
plt.title("Hashtags used in Tweets per Day Jan-July in 2020")
plt.legend()
plt.tight_layout()
plt.savefig('alternative')
plt.close()
