"""
Compute the number of inversions in the file IntegerArray.txt
"""

def sort_and_count(A, n):
    if n == 1:
        return (A, 0)
    else:
        half_index = n // 2
        
        # count first half of A
        (B,x) = sort_and_count(A[:half_index], half_index)
        
        # cound second half of A
        (C,y) = sort_and_count(A[half_index:], n - half_index)

        # count split inversions
        D = []
        i = 0
        j = 0
        z = 0
        while i < len(B) and j < len(C):
            if B[i] < C[j]:
                D.append(B[i])
                i += 1
            elif C[j] < B[i]:
                D.append(C[j])
                j += 1
                z += len(B) - i
        D += B[i:]
        D += C[j:]
        
    return (D, x + y + z)

with open("IntegerArray.txt", "r") as f:
    ints = []
    for line in f:
        ints.append(int(line))

n = len(ints)
print(sort_and_count(ints,n)[1]) # answer = 2407905288

