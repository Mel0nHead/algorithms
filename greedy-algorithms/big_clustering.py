import dset

file = open('./big_clustering.txt', 'r')

numberOfNodes = 0
numberOfBits = 0
nodes = [] # tracks the value for each node
myDict = {} # key is a value, corresponding value is the array of nodes with that value. e.g. 27: [1,2,4]
unionsArr = [] # keeps track of the union of each node

for line in file:
    arr = line.split()

    if len(arr) > 2:
        binaryString = ''.join(arr)
        intValue = int(binaryString,2)
        nodes.append(intValue)
    else:
        numberOfNodes,numberOfBits = int(arr[0]), int(arr[1])

for value in nodes:
    myDict[value] = []    

for i in range(0, numberOfNodes):
    value = nodes[i]
    myDict[value] += [i+1]
    unionsArr.append(dset.Set())

# bit masks are used to find the nodes which have a hamming distance of < 3 from each other
maskArr = [1 << i for i in range(numberOfBits)] + [2 << i for i in range(numberOfBits)] + [0]

for mask in maskArr:
    for value in myDict.keys():
        # XOR and mask
        value2 = value ^ mask
        # if resulting value is a key in the map
        if value2 in myDict:
            nodes = myDict[value] + myDict[value2]
            firstNode = nodes.pop(0)
            firstNodeUnion = unionsArr[firstNode - 1]

            # union all the values for value and value2
            for n in nodes:
                dset.union(firstNodeUnion, unionsArr[n - 1]) # note: the n - 1 is because the 1st node is stored at index 0

print(dset.groups())