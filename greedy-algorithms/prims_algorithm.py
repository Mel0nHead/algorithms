# Prim's algorithm
# Used to find the minimum spanning tree of a connected, undirected graph with weighted edges
# O(nm) for naive implementation; O(mlog(n)) for heap implementation

# Each edge will be in the format [head_node, tail_node, edge_weight]
file = open('./prim.txt', 'r')
allEdges = []
visitedNodes = {}
numberOfNodes = 0
numberOfEdges = 0

for line in file:
    edge = [int(i) for i in line.split()]

    if len(edge) > 2:
        allEdges.append(edge)

    else:
        numberOfNodes = edge[0]
        numberOfEdges = edge[1]

# Pick an arbitary node to start
startNode = allEdges[0][0]
visitedNodes[startNode] = 1
totalMSTWeight = 0 # We need to calculate the sum of the weights of all the edges in the MST

# While there are still unvisited nodes
while len(visitedNodes.keys()) != numberOfNodes:
    # out of all of the edges where one node is in X, the other is not, pick the one with smallest weight
    smallestEdge = [0,0,100000000000]

    for edge in allEdges:
        if edge[0] in visitedNodes and edge[1] not in visitedNodes:
            if edge[2] < smallestEdge[2]:
                smallestEdge = edge
        elif edge[1] in visitedNodes and edge[0] not in visitedNodes:
            if edge[2] < smallestEdge[2]:
                smallestEdge = edge

    # add this chosen edge to T
    totalMSTWeight += smallestEdge[2]
    # add the not yet seen node of this edge to X
    visitedNodes[smallestEdge[0]] = 1
    visitedNodes[smallestEdge[1]] = 1

print(totalMSTWeight)
