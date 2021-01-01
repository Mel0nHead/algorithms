# Kosaraju's Two-pass algorithm
# This is a modification of the Depth-First Search algorithm, used to compute the strongly connected components of a graph
# Assumes that the input is a directed graph with n nodes, m edges
# It has a Big-O of n + m

def generateGraph():
    file = open("./karger_data.txt","r")
    edges = []
    discoveredNodes = {}

    for line in file:
        edge = [int(i) for i in line.split()] # e.g. [1,3]
        edges.append(edge)
        discoveredNodes[edge[0]] = False
        discoveredNodes[edge[1]] = False

    graph = {
        'edges': edges,
        'discoveredNodes': discoveredNodes
    }
    return graph

def depthFirstSearch(graph, chosenNode):
    # mark node as discovered
    graph['discoveredNodes'][chosenNode] = True

    # find all edges that have chosenNode as a tail (chosenNode -> i)
    newEdges = [e for e in graph['edges'] if e[0] == chosenNode]

    # for each edge, if head node is undiscovered, call depthFirstSearch(graph, headNode)
    for edge in newEdges:
        headNode = edge[1]
        if graph['discoveredNodes'][headNode] == False:
            depthFirstSearch(graph, headNode)

# Run DFS on the reversed graph (edges have been reversed), calculating the 'finishing time' of each node
# Run DFS on the graph, in descending order of 'finishing time' from previous DFS call