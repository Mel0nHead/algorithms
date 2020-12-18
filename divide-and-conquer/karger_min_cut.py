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

# In the format {originalLabel: newLabel}, so that we know which nodes are merged with which
nodeLookup = {}
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

print(nodeLookup)
print(nodesAndEdges)

# def kargerMinCut(graph):
    # While there are more than 2 nodes
    # Randomly select an edge
    # merge the two nodes attached to the edge into one node
    # remove any self loops

    # Finally, return the cut defined by the final two edges

    # Remember to run this multiple times (with different seeds), making sure to remember the best answer