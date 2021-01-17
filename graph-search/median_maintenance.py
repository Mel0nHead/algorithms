# This algorithm uses the heap data structure for median maintenance
# It is a computationally efficient way of keeping track of the median of a group of numbers, assuming that there is a stream of integers 
# that arrive one at a time
import heapq
import math

# Start with two heaps:
# heap_low, which is a max-heap that stores the smaller 50% of the numbers
heap_low = [] # numbers should be multiplied by -1 every time they are inserted/extracted from this heap
heapq.heapify(heap_low)
# heap_high, which is a min-heap that store the larger 50% of the numbers
heap_high = []
heapq.heapify(heap_high)

medians = []
file = open("./heap.txt","r")
count = 0

for line in file:
    count += 1
    print(count)
    incoming_number = int(line)

    # if it is less than or equal to the min of heap_high, it gets inserted into heap_low
    if len(heap_low) == 0 or incoming_number <= heap_low[0] * -1:
        heapq.heappush(heap_low, incoming_number * -1)
        heapq.heapify(heap_low)
    # otherwise, it gets inserted into heap_high
    else:
        heapq.heappush(heap_high, incoming_number)
        heapq.heapify(heap_high)

    # after insertion, it is important to ensure that the two heaps are balanced
    balanced_split = math.ceil(count / 2)

    if len(heap_low) > balanced_split:
        max_item = heapq.heappop(heap_low) * -1
        heapq.heappush(heap_high, max_item)
        heapq.heapify(heap_high)
        heapq.heapify(heap_low)

    if len(heap_high) > balanced_split:
        min_item = heapq.heappop(heap_high)
        heapq.heappush(heap_low, min_item * -1)
        heapq.heapify(heap_high)
        heapq.heapify(heap_low)

    # you can then calculate the median by extracting the max/min from the bigger of the two heaps
    if len(heap_high) > len(heap_low):
        median = heap_high[0]
        medians.append(median)
    else:
        median = heap_low[0] * -1
        medians.append(median)

print(sum(medians) % 10000)