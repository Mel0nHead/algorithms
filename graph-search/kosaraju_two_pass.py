# Kosaraju's Two-pass algorithm
# This is a modification of the Depth-First Search algorithm, used to compute the strongly connected components of a graph
# Assumes that the input is a directed graph with n nodes, m edges
# It has a Big-O of n + m
import copy

def generateGraph():
    file = open("./scc.txt","r")
    edges = []
    discoveredNodes = {}

    for line in file:
        edge = [int(i) for i in line.split()] # e.g. [1,3]
        edges.append(edge)
        discoveredNodes[edge[0]] = False
        discoveredNodes[edge[1]] = False

    discoveredNodesCopy = copy.deepcopy(discoveredNodes)

    graph = {
        'edges': edges,
        'discoveredNodes': discoveredNodes,
        'discoveredNodesSecondPass': discoveredNodesCopy,
        'finishingTimes': {},
        'leaders': {},
        'finishingTimeCounter': 0
    }
    return graph

def depthFirstSearchFirstPass(graph, chosenNode):
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
            depthFirstSearchFirstPass(graph, headNode)

    graph['finishingTimeCounter'] += 1
    graph['finishingTimes'][graph['finishingTimeCounter']] = chosenNode

def depthFirstSearchSecondPass(graph, chosenNode, currentLeader):
    tailIndex = 0
    headIndex = 1

    if currentLeader in graph['leaders']:
        graph['leaders'][currentLeader] += 1
    else:
        graph['leaders'][currentLeader] = 1

    # mark node as discovered
    graph['discoveredNodesSecondPass'][chosenNode] = True

    # find all edges that have chosenNode as a tail (chosenNode -> i)
    newEdges = [e for e in graph['edges'] if e[tailIndex] == chosenNode]

    # for each edge, if head node is undiscovered, call depthFirstSearch(graph, headNode)
    for edge in newEdges:
        headNode = edge[headIndex]
        if graph['discoveredNodesSecondPass'][headNode] == False:
            depthFirstSearchSecondPass(graph, headNode, currentLeader)

def kosarajuTwoPass(graph):
    # Run DFS on the reversed graph (edges have been reversed), calculating the 'finishing time' of each node
    n = len(graph['discoveredNodes'].keys())

    for i in range(n, 0, -1):
        print('first pass - iteration: ' + str(i))
        if graph['discoveredNodes'][i] == False:
            depthFirstSearchFirstPass(graph, i)

    # Run DFS on the non-reversed graph, in descending order of 'finishing time' from previous DFS call
    for j in range(n, 0, -1):
        print('second pass - iteration: ' + str(j))
        originalNodeLabel = graph['finishingTimes'][j]
        if graph['discoveredNodesSecondPass'][originalNodeLabel] == False:
            leader = originalNodeLabel
            depthFirstSearchSecondPass(graph, originalNodeLabel, leader)

    sscSizeArray = list(graph['leaders'].values())
    sscSizeArray.sort(reverse=True)
    return sscSizeArray[0:5]

# Currently takes ~15 seconds to do 100 iterations of the first pass algo
newGraph = generateGraph()
arr = kosarajuTwoPass(newGraph)
print(arr)