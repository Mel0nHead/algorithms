# Kosaraju's Two-pass algorithm
# This is a modification of the Depth-First Search algorithm, used to compute the strongly connected components of a graph
# Assumes that the input is a directed graph with n nodes, m edges
# It has a Big-O of n + m

def generateGraph():
    file = open("./kosaraju_data.txt","r")
    edges = []
    discoveredNodes = {}

    for line in file:
        edge = [int(i) for i in line.split()] # e.g. [1,3]
        edges.append(edge)
        discoveredNodes[edge[0]] = False
        discoveredNodes[edge[1]] = False

    graph = {
        'edges': edges,
        'discoveredNodes': discoveredNodes,
        'finishingTimes': {},
        'leaders': {}
    }
    return graph

def depthFirstSearchFirstPass(graph, chosenNode, finishingTime):
    # reverse all the edges
    tailIndex = 1
    headIndex = 0

    # mark node as discovered
    graph['discoveredNodes'][chosenNode] = True

    # find all edges that have chosenNode as a tail (chosenNode -> i)
    newEdges = [e for e in graph['edges'] if e[tailIndex] == chosenNode]

    # for each edge, if head node is undiscovered, call depthFirstSearch(graph, headNode)
    for edge in newEdges:
        headNode = edge[headIndex]
        if graph['discoveredNodes'][headNode] == False:
            depthFirstSearchFirstPass(graph, headNode, finishingTime)

    finishingTime += 1
    graph['finishingTimes'][finishingTime] = chosenNode

def depthFirstSearchSecondPass(graph, chosenNode, currentLeader):
    tailIndex = 0
    headIndex = 1

    graph['leaders'][chosenNode] = currentLeader
    # mark node as discovered
    graph['discoveredNodes'][chosenNode] = True

    # find all edges that have chosenNode as a tail (chosenNode -> i)
    newEdges = [e for e in graph['edges'] if e[tailIndex] == chosenNode]

    # for each edge, if head node is undiscovered, call depthFirstSearch(graph, headNode)
    for edge in newEdges:
        headNode = edge[headIndex]
        if graph['discoveredNodes'][headNode] == False:
            depthFirstSearchSecondPass(graph, headNode, currentLeader)

def kosarajuTwoPass(graph):
    # Run DFS on the reversed graph (edges have been reversed), calculating the 'finishing time' of each node
    finishingTime = 0
    n = len(graph['discoveredNodes'].keys())

    for i in range(n, 0, -1):
        if graph['discoveredNodes'][i] == False:
            depthFirstSearchFirstPass(graph, i, finishingTime)

    # Run DFS on the non-reversed graph, in descending order of 'finishing time' from previous DFS call
    for j in range(n, 0, -1):
        originalNodeLabel = graph['finishingTimes'][j]
        if graph['discoveredNodes'][originalNodeLabel] == False:
            leader = originalNodeLabel
            depthFirstSearchSecondPass(graph, originalNodeLabel, leader)
