# Clustering algorithm
# If we have a set of points, group the points into k clusters such that we maximise the spacing
# The `spacing` of a clustering is the distance between the closest two seperated (in different clusters) points
import dset

file = open('./clustering.txt', 'r')
k = 4 # target number of clusters
numberOfClusters = 0
edges = []

for line in file:
    numberArray = [int(i) for i in line.split()]

    if len(numberArray) == 1:
        numberOfClusters = numberArray[0] # Initially, each point will be in its own cluster
    else:
        # Each edge is in the format [node_a, node_b, distance]
        edges.append(numberArray)

def getWeight(edge):
    return edge[2]

# Sort the `edges` in increasing order of weight - this operation has O(mlog(n))
edges.sort(key=getWeight, reverse=False)
nodeClusters = [dset.Set() for i in range(0,numberOfClusters)] # node 1 at index 0, node 2 at index 1 etc...

while numberOfClusters > k:
    for e in edges:
        [nodeA, nodeB, weight] = e
        nodeAGroup, nodeBGroup = nodeClusters[nodeA - 1], nodeClusters[nodeB - 1]

        # Find the closest pair of seperated points
        if dset.find(nodeAGroup) != dset.find(nodeBGroup):
            # Merge the two clusters containing these two points
            dset.union(nodeAGroup, nodeBGroup)
            numberOfClusters -= 1
            break

for e in edges:
    [nodeA, nodeB, weight] = e
    nodeAGroup, nodeBGroup = nodeClusters[nodeA - 1], nodeClusters[nodeB - 1]

    # Find the closest pair of seperated points
    if dset.find(nodeAGroup) != dset.find(nodeBGroup):
        # Merge the two clusters containing these two points
        print(weight)
        break