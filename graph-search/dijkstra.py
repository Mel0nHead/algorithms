# Dijkstra's Shortest-Path Algorithm
# Given a source node s, this finds the shortest path from s to all other nodes in the graph
# All edge weights have to be non-negative for the algorithm to work
# Simple implementation has O(nm), heap implementation has O(m*log(n)) (graph has n nodes, m edges)

exploredCount = 0
N = 0 # number of nodes
adjArray = [] # will contain all the edges (twice) in the formate [fromNode, toNode, edgeWeight]
explored = [] # index corresponds to each node - will be True or False
shortestPaths = [] # index corresponds to each node - will be integer between 1 and 1000000

file = open("dijkstra.txt", "r")
data = file.readlines()

for line in data:
    strArr = line.split()
    tail = strArr.pop(0)
    explored.append(False)
    shortestPaths.append(0) 
    N += 1
    
    for s in strArr:
        edge = [tail] + s.split(',')
        edge = [int(i) for i in edge]
        adjArray.append(edge)
        
# mark the source node as explored (in this case we have just chosen the first node)
explored[0] = True
exploredCount += 1

# While there are still nodes that have not bee explored
while exploredCount < N:
    minGreedyCriterion = 1000000
    nodeToPullIn = None # TODO: need a better value than this

    # Find all edges going from explored to unexplored
    for [fromNode, toNode, weight] in adjArray:
        if explored[fromNode - 1] == True and explored[toNode - 1] == False:
        # Amongst them, find the one with the smallest dijkstra greedy criterion
            if shortestPaths[fromNode - 1] + weight < minGreedyCriterion:
                nodeToPullIn = toNode
                minGreedyCriterion = shortestPaths[fromNode - 1] + weight

    # explore the node that has the minimum dijkstra's greedy criterion
    explored[nodeToPullIn - 1] = True
    # increment explored count
    exploredCount += 1
    # update the shortest path of newly added node
    shortestPaths[nodeToPullIn - 1] = minGreedyCriterion

indices = [7,37,59,82,99,115,133,165,188,197]
result = [shortestPaths[i-1] for i in indices]
print(result)