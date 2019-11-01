"""
You are given a sorted (from smallest to largest)
array A of n distinct integers which can be
positive, negative, or zero. You want to decide
whether or not there is an index i such that
A[i] = i. Design the fastest algorithm that you
can for solving this problem.
"""

def is_special(A):
    start = 0
    end = len(A) - 1
    
    # base case
    if start == end:
        if A[start] == start:
            return True

    while end > start:
        
        # two element case
        if end == (start + 1) and (A[start] == start or A[end] == end):
            return True
        
        i = (start + end) // 2
        if A[i] == i:
            return True
        elif A[i] > i:
            end = i
        else:
            start = i + 1

    return False
    
A = [0]
print(is_special(A)) # True

A = [0, 2]
print(is_special(A)) # True

A = [-1, 1]
print(is_special(A)) # True

A = [0, 1, 3, 10]
print(is_special(A)) # True

A = [2, 5, 9, 10]
print(is_special(A)) # False

# edge case
A = [0, 2, 3]
print(is_special(A)) # True

# edge case
A = [-1, 1, 2]
print(is_special(A)) # True