# Karger's Random Contraction algorithm
# Used for calculating the minimum cut of an undirected graph
# Assuming the original graph has n nodes, m edges, complexity is O(m*n^2)
# Parallel edges are allowed
import random
import copy
import math

def generateGraph():
    nodeLookup = {} # In the format { originalLabel: newLabel }, so that we know which nodes are merged with which
    edges = [] # An array of all the edges. Note: (a,b) will be in twice - [a,b] and [b,a]
    nodesAndEdges = {}

    file = open("./karger_data.txt","r")
    for line in file:
        stringArr = line.split()
        results = [int(i) for i in stringArr]
        nodeLabel = results.pop(0)

        nodesAndEdges[nodeLabel] = {
            'mergedWith': [nodeLabel],
            'edges': results
        }

        nodeLookup[nodeLabel] = nodeLabel

        for res in results:
            edges.append([nodeLabel, res])

    graph = {
        'nodeLookup': nodeLookup,
        'edges': edges,
        'nodesAndEdges': nodesAndEdges
    }
    return graph

def contractEdge(graph, edgeIndex):
    # check if the chosen edge is a self loop
    [nodeA, nodeB] = graph['edges'].pop(edgeIndex)
    firstNode = graph['nodeLookup'][nodeA]
    secondNode = graph['nodeLookup'][nodeB]

    if firstNode == secondNode: # Means that chosen edge is a self loop
        return

    # second will get merged into first
    graph['edges'].remove([nodeB, nodeA]) # E.g. if [a,b] was selected, then remove [b,a] as they correspond to the same edge

    secondNodeInfo = graph['nodesAndEdges'].pop(secondNode, None)

    # merge secondNode's 'mergedWith' and 'edges' to the first node
    graph['nodesAndEdges'][firstNode]['mergedWith'] += secondNodeInfo['mergedWith']
    graph['nodesAndEdges'][firstNode]['edges'] += secondNodeInfo['edges']

    # update the lookup
    for index in secondNodeInfo['mergedWith']:
        graph['nodeLookup'][index] = firstNode

def kargerMinCut(graph):

    # While there are more than 2 nodes
    if len(graph['nodesAndEdges']) > 2:
        # Randomly select an edge
        randomIndex = random.randint(0, len(graph['edges']) - 1)
        contractEdge(graph, randomIndex)
        cuts = kargerMinCut(graph)
        return cuts

    # Finally, return the cut defined by the final two edges
    else:
        firstNode = graph['nodesAndEdges'].keys()[0]

        # remove any self loops
        newEdges = []
        for edge in graph['nodesAndEdges'][firstNode]['edges']:
            if edge not in graph['nodesAndEdges'][firstNode]['mergedWith']:
                newEdges.append(edge)

        return len(newEdges)

# Since the Karger algorithm is not guaranteed to always return the minimum cut, we have to run in many times and take
# the lowest output
def repeatKarger(graph):
    lowestCut = None
    n = len(graph['nodeLookup']) # number of nodes
    N = (n**2)*math.log(n) # number of trials we should do
    i = 0

    while i < N:
        i += 1
        print('Currently on iteration ' + str(i) + ' out of ' + str(int(N)))
        graphCopy = copy.deepcopy(graph)
        minCut = kargerMinCut(graphCopy)

        if lowestCut == None:
            lowestCut = minCut
        elif minCut < lowestCut:
            lowestCut = minCut

    return lowestCut

# Currently takes ~1m 18s to complete 1000 iterations
newGraph = generateGraph()
minimumCut = repeatKarger(newGraph)
print(minimumCut)