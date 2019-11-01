"""
You are a given a unimodal array of n distinct elements,
meaning that its entries are in increasing order up until
its maximum element, after which its elements are in
decreasing order. Give an algorithm to compute the
maximum element that runs in O(log n) time.
"""

def max_unimodal(L):
    start = 0
    end = len(L) - 1
    
    # base case
    if start == end:
        return L[start]
        
    while end > start:
        
        # two element cases
        if end == (start + 1) and L[start] > L[end]:
            return L[start]
            
        elif end == (start + 1) and L[start] < L[end]:
            return L[end]

        # binary search 
        mid = (start + end) // 2
        if L[mid] > L[mid-1] and L[mid] > L[mid+1]:
            return L[mid]
        elif L[mid] > L[mid-1]:
            start = mid + 1
        else:
            end = mid 

# base case
L = [5]
print(max_unimodal(L)) # 5

L = [1, 2]
print(max_unimodal(L)) # 2

L = [2, 1]
print(max_unimodal(L)) # 2

L = [1, 2, 6, 4, 3]
print(max_unimodal(L)) # 6

L = [1, 7, 6, 4, 3]
print(max_unimodal(L)) # 7

# edge case
L = [4, 3, 2, 1]
print(max_unimodal(L)) # 4

# edge case
L = [1, 2, 3, 4]
print(max_unimodal(L)) # 4