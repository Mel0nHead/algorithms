# This algorithm uses a hash table to solve the 2 sum problem, and therefore has O(n)
# Given an array of n integers, and a value t, does there exist a distinct pair of integers x and y in the array such that x + y = t?
# In our specific implementation, we need to solve for each t in [-10000, 10000], and count for how many values of t an answer exists

H = {}
file = open("./two_sum_data.txt","r")

# Insert all elements of the array into a hash table
for line in file:
    print('processing line ' + str(line) + ' of file')
    H[int(line)] = 0

def two_sum(hashTable, targetValue):
    doesSolutionExist = False

    # For each value x in the hash table, try and lookup targetValue - x
    for x in hashTable.keys():
        y = targetValue - x
        
        # If x and targetValue - x exist in the hash table, and x != targetValue - x, then it is a valid solution
        if x != y and y in hashTable:
            doesSolutionExist = True
            break
    
    return doesSolutionExist

def iterate_two_sum(hashTable, lowerBound, upperBound):
    totalCount = 0

    for t in range(lowerBound, upperBound + 1):
        print('target value: ' + str(t))
        if two_sum(hashTable, t) == True:
            totalCount += 1
    
    return totalCount
# Currently very slow: takes ~ 2 mins 4 seconds to iterate through 500 values of t
print('FINAL ANSWER', iterate_two_sum(H, -10000, 10000))