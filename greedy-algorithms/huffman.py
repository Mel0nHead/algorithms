# Huffman coding
# Given a set of symbols, find a binary encoding for each symbol such that the encoding is prefix-free, and such that the sum of
# the expected lengths of each encoded symbol is minimised.
# Simple implementation: O(n*log(n)); Priority queue implementation; O(n)
import heapq

file = open('./huffman.txt', 'r')
weights = [] # list of tuples, each in the form (weight, label)
lengths = [] # list of encoding lengths, where the index of the array corresponds to the label
index = 0

for line in file:
    weights.append((int(line), str(index)))
    lengths.append(0)
    index += 1

numberOfSymbols = weights.pop(0)[0]

# put all weights into a min-heap
heapq.heapify(weights)

# while there is more than one node in the queue
while len(weights) > 1:
    # remove the two nodes of highest priority from the queue
    smallest = heapq.heappop(weights)
    secondSmallest = heapq.heappop(weights)
    mergedItem = (smallest[0] + secondSmallest[0], smallest[1] + secondSmallest[1])

    # increment the length for all symbols who have been merged
    symbols = [int(s) for s in mergedItem[1]]
    for s in symbols:
        lengths[s] += 1

    # merge them to become a single point (with sum of the weights), and insert into the heap
    heapq.heappush(weights, mergedItem)

lengths.pop(0) # first item was just a placeholder
print(max(lengths))
print(min(lengths))

