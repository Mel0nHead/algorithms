# Clustering algorithm
# If we have a set of points, group the points into k clusters such that we maximise the spacing
# The `spacing` of a clustering is the distance between the closest two seperated (in different clusters) points 

file = open('./clustering.txt', 'r')
k = 4 # target number of clusters
numberOfClusters = 0
edges = []

for line in file:
    numberArray = [int(i) for i in line]

    if len(numberArray) == 1:
        numberOfClusters = numberArray[0] # Initially, each point will be in its own cluster
    else:
        # Each edge is in the format [node_a, node_b, distance]
        edges.append(numberArray)

# Sort the `edges` in decreasing order of weight - this has O(mlog(n))


# Use a Union-Find data structure to track which node is in which cluster

# while the number of clusters > k
# Find the closest pair of seperated points
# Merge the two clusters containing these two points