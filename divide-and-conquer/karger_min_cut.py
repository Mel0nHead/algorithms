# Karger's Random Contraction algorithm
# Used for calculating the minimum cut of an undirected graph
# Assuming the original graph has n nodes, m edges, complexity is O(m*n^2)
# Parallel edges are allowed

# [[1], 2,3,4]
# [[2], 1,3,4]
# [[3], 2,'1',4]
# [[4], 2,3,1]

# [[1,3], 2,4,2,4]
# [[2], 1,3,4]
# [[4], 2,'3',1]

# [[1,3,4], 2,2,2]
# [[2], 1,3,4]

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
    # second will get merged into first
    [nodeA, nodeB] = graph['edges'].pop(edgeIndex)
    graph['edges'].remove([nodeB, nodeA]) # E.g. if [a,b] was selected, then remove [b,a] as they correspond to the same edge
    firstNode = graph['nodeLookup'][nodeA]
    secondNode = graph['nodeLookup'][nodeB]

    secondNodeInfo = graph['nodesAndEdges'].pop(secondNode, None)

    # merge secondNode's 'mergedWith' and 'edges' to the first node
    graph['nodesAndEdges'][firstNode]['mergedWith'] += secondNodeInfo['mergedWith']
    graph['nodesAndEdges'][firstNode]['edges'] += secondNodeInfo['edges']

    # update the lookup
    for index in secondNodeInfo['mergedWith']:
        graph['nodeLookup'][index] = firstNode

    # remove any self loops
    newEdges = []
    for edge in graph['nodesAndEdges'][firstNode]['edges']:
        if edge not in graph['nodesAndEdges'][firstNode]['mergedWith']:
            newEdges.append(edge)

    graph['nodesAndEdges'][firstNode]['edges'] = newEdges

def kargerMinCut(graph):

    # While there are more than 2 nodes
    if len(graph['nodesAndEdges']) > 2:
        # Randomly select an edge
        randomIndex = 3 # TODO: make it random
        contractEdge(graph, randomIndex)
        cuts = kargerMinCut(graph)
        return cuts

    # Finally, return the cut defined by the final two edges
    else:
        return len(graph['edges']) / 2

    # Remember to run this multiple times (with different seeds), making sure to remember the best answer

newGraph = generateGraph()
contractEdge(newGraph, 3) # [1,7]
print(len(newGraph['nodesAndEdges']))