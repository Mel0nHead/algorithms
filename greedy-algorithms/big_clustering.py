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

maskArr = [1 << i for i in range(numberOfBits)] + [2 << i for i in range(numberOfBits)] + [0]

for mask in maskArr:
    for value in myDict.keys():
        