"""
The file (Quicksort.txt) contains all of the integers between 1 and 10,000
(inclusive, with no repeats) in unsorted order. The integer in the ith row of
the file gives you the ith entry of an input array.

Your task is to compute the total number of comparisons used to sort the given
input file by QuickSort. As you know, the number of comparisons depends on which
elements are chosen as pivots, so we'll ask you to explore three different pivoting
rules.

You should not count comparisons one-by-one. Rather, when there is a recursive
call on a subarray of length m, you should simply add m - 1 to your running total
of comparisons. (This is because the pivot element is compared to each of the other 
m - 1 elements in the subarray in this recursive call.)
"""

# quicksort algorithm
    # if n = 1, return A
    # p = ChoosePivot(A, n)
    # partition A around p
    # recursively sort 1st partition
    # recursively sort 2nd partition

def quick_sort(A, first, last):
    """
    Sorts and counts number of comparisons, quick_sort.count
    """
    
    # zero and 1 element case
    if last - first + 1 <= 1:
        return

    quick_sort.count += last - first
    p = choose_pivot(A, first, last)
    A[first], A[p] = A[p], A[first]

    i = first + 1
    for j in range(first+1, last+1):
        if A[j] < A[first]:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[first], A[i-1] = A[i-1], A[first]

    quick_sort(A, first, i-2)
    quick_sort(A, i, last)

quick_sort.count = 0



def choose_pivot(A, first, last):
    
    # Case 1: first element as pivot
    # return first
    
    # Case 2: last element as pivot
    # return last
    
    # Case 3: median of [first, middle, last] as pivot
    middle = (first + last) // 2
    pivots = sorted([A[first], A[middle], A[last]])
    return A.index(pivots[1])


with open("QuickSort.txt", "r") as f:
    A = []
    for line in f:
        A.append(int(line))

# Case 1: first element as pivot
# answer = 162085

# Case 2: last element as pivot
# asnwer = 164123

# Case 3: median of [first, middle, last] as pivot
# answer = 138382

quick_sort(A, 0, len(A)-1)
print(quick_sort.count)
