# For this algorithm, we are going to use dynamic programming to find the maximum weighted independent set (WIS) of a path graph
# This has O(n)

A = [] # index i stores the max WIS value for G_i (the subgraph containing the first i nodes of G)
Graph = [] # this is the intial path graph
optimumNodes = [] # this is an array of all of the nodes in the max WIS

file = open('./dynamic.txt', 'r')

for line in file:
    Graph.append(int(line))
    A.append(None)

n = Graph.pop(0)
A[0] = 0
A[1] = Graph[0]

# Given a graph G, recursively...
# Compute S' = the WIS of G' (G with the right-most node removed)
# Compute S'' = the WIS of G'' (G with the two right-most nodes removed)
# Return the maximum of S' and S'' union v_n
for i in range(2, n + 1):
    A[i] = max(A[i - 1], A[i - 2] + Graph[i - 1])

# Reconstruction step, to calculate which nodes are in the max WIS
i = n
while i >= 1:
    if A[i - 1] >=  A[i - 2] + Graph[i - 1]:
        i -= 1
    else:
        optimumNodes.append(i)
        i -= 2

def inOptimum(x):
    if x in optimumNodes:
        return 1
    else:
        return 0

desiredNodes = [1, 2, 3, 4, 17, 117, 517, 997]
result = map(inOptimum, desiredNodes)
print(result)

