"""
You are given as input an unsorted array (L) of n distinct numbers,
where n is a power of 2. Give an algorithm that identifies
the second-largest number in the array, and that uses at most
n + log(n) - 2 comparisons
"""

# Step 1: tournament style comparison between adjacent numbers (winner is max number)
# n - 1 comparisons

# Step 2: find max of all max numbers opponents
# logn - 1 comparisons 

# total comparisons = n + logn - 2

def second_largest(L):
    n = len(L) // 2
    battles = {} # key: number of L, value: array of numbers key compared against
    
    # find the max 
    while (n >= 1):
        round_winners = []
        for i in range (0, n):
            if L[2 * i] > L[2 * i + 1]:
                round_winners.append(L[2 * i])
                if L[2 * i] not in battles:
                    battles[L[2 * i]] = []
                battles[L[2 * i]].append(L[2 * i + 1])
            else:
                round_winners.append(L[2 * i + 1])
                if L[2 * i + 1] not in battles:
                    battles[L[2 * i + 1]] = []
                battles[L[2 * i + 1]].append(L[2 * i])
        L = round_winners
        n = n // 2  
    winner = L[0] 
    
    # return second largest
    return max(battles[winner])

L = [1, 2]
print(second_largest(L))

L = [3, 6, 1, 0]
print(second_largest(L))

L = [9, 1, 4, 10]
print(second_largest(L))

L = [10, 9, 5, 4, 11, 100, 120, 110]
print(second_largest(L))
