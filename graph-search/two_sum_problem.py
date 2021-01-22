# This algorithm uses a hash table to solve the 2 sum problem, and therefore has O(n)
# Given an array of n integers, and a value t, does there exist a distinct pair of integers x and y in the array such that x + y = t?
# In our specific implementation, we need to solve for each t in [-10000, 10000], and count for how many values of t an answer exists
H = {}
file = open("./two_sum_data.txt","r")

# Insert all elements of the array into a hash table
for line in file:
    print('processing line ' + str(line) + ' of file')
    H[int(line)] = 0

totalCount = 0
hashKeys = H.keys()

for t in range(-10000, 10001):
    print('target value: ' + str(t))
    
    for x in hashKeys:
        y = t - x

        if x != y and y in H:
            totalCount += 1
            break
    

    
# Currently very slow: takes ~ 1 min 50 secs to iterate through 500 values of t
# It will take over 80 mins to complete the whole thing
print('***** FINAL ANSWER *****', totalCount)