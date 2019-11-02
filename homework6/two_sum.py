"""
The goal of this problem is to implement a variant of the 2-SUM algorithm
(covered in the Week 6 lecture on hash table applications).

The file contains 1 million integers, both positive and negative (there might be
some repetitions!).This is your array of integers, with the ith row of the file
specifying the ith entry of the array.

Your task is to compute the number of target values t in the interval
[-10000,10000] (inclusive) such that there are distinct numbers x, y in the input
file that satisfy x + y = t.

(NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)
"""

import bisect

a = []
with open('algo1-programming_prob-2sum.txt', 'r') as f:
    for line in f:
        a.append(int(line.strip()))
a.sort()

start, end = -10000, 10000 # interval (inclusive) for targets
targets = set()
for x in a:
    lower = bisect.bisect_left(a, start - x)
    upper = bisect.bisect_right(a, end - x)
    for y in a[lower:upper]:
        if x != y:
            targets.add(x + y)
            
print(len(targets))
