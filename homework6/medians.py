"""
The goal of this problem is to implement the "Median Maintenance" algorithm
(covered in the Week 5 lecture on heap applications). The text file contains a
list of the integers from 1 to 10000 in unsorted order; you should treat this as
a stream of numbers, arriving one by one. Letting xi denote the ith number of the
file, the kth median mk is defined as the median of the numbers x1,..., xk. (So,
if k is odd, then mk is ((k + 1) / 2)th smallest number among x1,..., xk; if k 
is even, then mk is the (k / 2)th smallest number among x1,..., xk.)

In the box below you should type the sum of these 10000 medians, modulo 10000
(i.e., only the last 4 digits). That is, you should compute:

(m1 + ... + m10000)mod10000

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and
search-tree-based implementations of the algorithm.
"""

import heaps

input_file = "Median.txt"

def rebalance_heaps(A, B):
    """
    Rebalances heaps A and B such that size of A is equal or
    greater than size of B by 1.
    """
    while (A.size - B.size > 1):
        i = A.pop()
        B.push(i)

    while (B.size - A.size >= 1):
        i = B.pop()
        A.push(i)

max = heaps.max_heap([])
min = heaps.min_heap([])
medians = []

with open(input_file, "r") as f:
    for line in f:
        x = int(line.strip())

        if (max.size == 0):
            max.push(x)
        else:
            if (x > max.peek()):
                min.push(x)
            elif (x < max.peek()):
                max.push(x)
        rebalance_heaps(max, min)
        medians.append(max.peek())

print(sum(medians)%10000) # answer = 1213
