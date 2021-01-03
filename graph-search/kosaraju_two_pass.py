# Kosaraju's Two-pass algorithm
# This is a modification of the Depth-First Search algorithm, used to compute the strongly connected components of a graph
# Assumes that the input is a directed graph with n nodes, m edges
# It has a Big-O of n + m
import copy

def generateGraph():
    file = open("./scc.txt","r")
    edges = {}
    reversedEdges = {}
    discoveredNodes = {}

    for line in file:
        print('processing data...')
        edge = [int(i) for i in line.split()] # e.g. [1,3]
        [tail, head] = edge

        if tail in edges:
            edges[tail].append(head)
        else:
            edges[tail] = [head]

        if head in reversedEdges:
            reversedEdges[head].append(tail)
        else:
            reversedEdges[head] = [tail]

        discoveredNodes[edge[0]] = False
        discoveredNodes[edge[1]] = False

    discoveredNodesCopy = copy.deepcopy(discoveredNodes)

    graph = {
        'edges': edges,
        'reversedEdges': reversedEdges,
        'discoveredNodes': discoveredNodes,
        'discoveredNodesSecondPass': discoveredNodesCopy,
        'finishingTimes': {},
        'leaders': {},
        'finishingTimeCounter': 0
    }
    return graph

def depthFirstSearchFirstPass(graph, chosenNode):
    # mark node as discovered
    graph['discoveredNodes'][chosenNode] = True

    # for each edge, if head node is undiscovered, call depthFirstSearch(graph, headNode)
    if chosenNode in graph['reversedEdges']:
        for node in graph['reversedEdges'][chosenNode]:
            if graph['discoveredNodes'][node] == False:
                depthFirstSearchFirstPass(graph, node)

    graph['finishingTimeCounter'] += 1
    graph['finishingTimes'][graph['finishingTimeCounter']] = chosenNode

def depthFirstSearchSecondPass(graph, chosenNode, currentLeader):
    if currentLeader in graph['leaders']:
        graph['leaders'][currentLeader] += 1
    else:
        graph['leaders'][currentLeader] = 1

    # mark node as discovered
    graph['discoveredNodesSecondPass'][chosenNode] = True

    # for each edge, if head node is undiscovered, call depthFirstSearch(graph, headNode)
    if chosenNode in graph['edges']:
        for node in graph['edges'][chosenNode]:
            if graph['discoveredNodesSecondPass'][node] == False:
                depthFirstSearchSecondPass(graph, node, currentLeader)

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