# Quick Sort - an algorithm used to sort an array of integers in ascending order
# There are multiple ways to choose a pivot, which determines the efficiency of splitting the array into sub-arrays
# The Big-O varies from n*log(n) to n^2, depending on how the pivot is chosen

# For this implementation, we are going to pick the median out of the first, middle and last element of the array
def get_median_pivot(array, lowest_index, highest_index):
    first = array[lowest_index]
    last = array[highest_index]
    median_index = (lowest_index + highest_index) // 2

    median = array[median_index]
    pivot_array = [first, median, last]
    pivot_array.sort()
    return pivot_array[1]



def partition(array, lowest_index, highest_index):
    pivot = get_median_pivot(array, lowest_index, highest_index)
    # As a pre-processing step, we switch the chosen pivot with the first element in the array
    pivot_index = array.index(pivot)
    array[pivot_index] = array[lowest_index]
    array[lowest_index] = pivot

    # i keeps track of where the partition is (smaller numbers to left, larger to right)
    i = lowest_index + 1
    # j keeps track of how many elements in the array we have evaluated
    for j in range(lowest_index + 1, highest_index + 1):
        if array[j] < pivot:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            i += 1

    # Finally, put the pivot in the right place, and return the pivot's index
    array[lowest_index] = array[i-1]
    array[i-1] = pivot
    return [i - 1, len(array[lowest_index: highest_index + 1]) - 1]

def quick_sort(array, lowest_index, highest_index):
    if (lowest_index < highest_index):
        # Sorts the array so that all elements less than the pivot are to the left, 
        # and all elements greater than the pivot are to the right. It then returns the index of the pivot
        [pivot_index, comparison_count] = partition(array, lowest_index, highest_index)
        # Sort the numbers to the left and right of the pivot
        sub_arr_comparison_count_1 = quick_sort(array, lowest_index, pivot_index - 1)
        sub_arr_comparison_count_2 = quick_sort(array, pivot_index + 1, highest_index)
        return comparison_count + sub_arr_comparison_count_1 + sub_arr_comparison_count_2

    else:
        return 0

massive_array = []

file = open("./quick_numbers_3.txt","r")
for line in file:
    massive_array.append(int(line))

print(quick_sort(massive_array,0, len(massive_array) - 1)) # should be 56
