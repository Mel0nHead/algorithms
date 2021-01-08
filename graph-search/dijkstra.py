# Dijkstra's Shortest-Path Algorithm
# Given a source node s, this finds the shortest path from s to all other nodes in the graph
# All edge weights have to be non-negative for the algorithm to work
# Simple implementation has O(nm), heap implementation has O(m*log(n)) (graph has n nodes, m edges)

# Node label: otherNode, edgeWeight
# If no path exists from s to some node n, then assign the shortest path value to be 1000000

#adjArray = [[1,2,3], [4,2,4]] # each item is an array in the form [fromNode, toNode, edgeWeight]
#explored =[False,False,False, False] # index corresponds to each node
#exploredCount = 0 # counts the number of Trues in explored
#shortestPaths = [0,0,0,0]

exploredCount = 0
adjArray = [] # will contain all the edges (twice) in the formate [fromNode, toNode, edgeWeight]
explored = [] # index corresponds to each node - will be True or False
shortestPaths = [] # index corresponds to each node - will be integer between 1 and 1000000

def createGraph():
    file = open("dijkstra.txt", "r")
    data = file.readlines()

    for line in data:
        strArr = line.split()
        tail = strArr.pop(0)
        explored.append(False)
        shortestPaths.append(1000000)
        
        for s in strArr:
            edge = [tail] + s.split(',')
            edge = [int(i) for i in edge]
            adjArray.append(edge)
        

createGraph()
print(shortestPaths)

# def dijkstra(graph):

    # While exploredCount is less than the total number of nodes

    # Find all edges going from explored to unexplored 
        # Amongst them, find the one with the smallest dijkstra greedy criterion
        # use the chosen one to determine which node to pull into explored 
        # increment explored count
        # update the shortest path of newly added node