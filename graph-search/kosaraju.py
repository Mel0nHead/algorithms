# node labels range from 1 to 875714. 875715 was used because of the range operator... range(875715) goes up to 875714.
# numberOfNodes = 875715
numberOfNodes = 13

# Adjacency representations of the graph and reverse graph
graph = [[] for i in range(numberOfNodes)]
reversedGraph = [[] for i in range(numberOfNodes)]

# The list index represents the node. If node i is unvisited then visited[i] == False and vice versa
visited = [False] * numberOfNodes

# The list below holds info about sccs. The index is the scc leader and the value is the size of the scc.
scc = [0] * numberOfNodes

stack = []  # Stack for DFS
order = []  # The finishing orders after the first pass


########################################################
# Importing the graphs
file = open("kosaraju_data.txt", "r")
data = file.readlines()

for line in data:
    [tail, head] = line.split() # e.g ['1', '3']
    graph[int(tail)] += [int(head)]
    reversedGraph[int(head)] += [int(tail)]


########################################################
# DFS on reverse graph

for node in range(numberOfNodes):
    # mark node as visited
    if visited[node] == False:
        stack.append(node)
        visited[node] = True

        while len(stack) > 0:
            # get last added item in the stack
            stackNode = stack[-1]
            isDone = True

            # check all the nodes that the stack node has edges to
            for head in reversedGraph[stackNode]:
                if visited[head] == False:
                    stack.append(head)
                    visited[head] = True
                    isDone = False

            # if the stack node has no more unexplored outgoing edges, remove it from the stack
            if isDone == True:
                removedNode = stack.pop()
                order.append(removedNode)



########################################################
# DFS on original graph

visited = [False] * len(visited)  # Resetting the visited variable
order.reverse()  # The nodes should be visited in reverse finishing times

for node in order:
    currentLeader = node

     # mark node as visited
    if visited[node] == False:
        stack.append(node)
        visited[node] = True

        while len(stack) > 0:
            # get last added item in the stack
            stackNode = stack[-1]
            isDone = True

            # check all the nodes that the stack node has edges to
            for head in graph[stackNode]:
                if visited[head] == False:
                    stack.append(head)
                    visited[head] = True
                    isDone = False

            # if the stack node has no more unexplored outgoing edges, remove it from the stack
            if isDone == True:
                stack.pop()
                scc[currentLeader] += 1

########################################################
# Getting the five biggest sccs
# TODO: find out why an extra 1 seems to get added to the output
scc.sort(reverse=True)
print(scc)
