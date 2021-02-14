# The Knapsack problem: given an input of n items (with each item i having a value v_i and size w_i), and a knapsack capacity C,
# find the maximum value subset of the n items such that the total size of the subset is less than or equal to C
# The solution is to use dynamic programming; it has O(nC)
import sys
sys.setrecursionlimit(3000)

# Import the data
file = open('./recursive_knapsack.txt', 'r')
items = [] # each item will be in the format [value, weight]

for line in file:
    arr = [int(x) for x in line.split()]
    items.append(arr)

[C, n] = items.pop(0)
answers = {}

# i items, x capacity
def knapsack(i, x):
    print(i, x)
    if i == 0:
        return 0

    [value, weight] = items[i - 1]
    key = str(i) + ',' + str(x)

    if key in answers:
        return answers[key]
    else:
        ans = 0
        if weight > x:
            ans = knapsack(i - 1, x)
        else:
            ans = max(knapsack(i - 1, x), knapsack(i-1, x-weight) + value)
        
        answers[key] = ans
        return ans

print(knapsack(n,C))