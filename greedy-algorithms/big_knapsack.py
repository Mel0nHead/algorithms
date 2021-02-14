# The Knapsack problem: given an input of n items (with each item i having a value v_i and size w_i), and a knapsack capacity C,
# find the maximum value subset of the n items such that the total size of the subset is less than or equal to C
# The solution is to use dynamic programming; it has O(nC)

# Import the data
file = open('./big_knapsack.txt', 'r')
items = [] # each item will be in the format [value, weight]
A = []

for line in file:
    arr = [int(x) for x in line.split()]
    items.append(arr)

[C, n] = items.pop(0)

for i in range(0, 2):
    A.append([0]* (C + 1)) # there will be two subarrays - one for previous answers, one for current answers

for i in range(1, n + 1): # 1, 2,...,n
    for x in range(0, C + 1): # 0, 1, 2,..., C
        [value, weight] = items[i - 1]

        if weight > x:
            A[1][x] = A[0][x]
        else:
            A[1][x] = max(A[0][x], A[0][x - weight] + value)


# print(A[n][C])