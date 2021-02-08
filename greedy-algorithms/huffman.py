# Huffman coding
# Given a set of symbols, find a binary encoding for each symbol such that the encoding is prefix-free, and such that the sum of
# the expected lengths of each encoded symbol is minimised.
# Simple implementation: O(n*log(n)); Priority queue implementation; O(n)

file = open('./huffman.txt', 'r')
weights = []

for line in file:
    weights.append(int(line))

numberOfSymbols = weights.pop(0)

# put all weights into a heap (remember to multiply by -1 so that smallest weight has highest priority)

# while there is more than one node in the queue
# remove the two nodes of highest priority from the queue
# 
