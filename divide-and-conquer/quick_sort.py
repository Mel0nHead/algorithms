# Quick Sort - an algorithm used to sort an array of integers in ascending order
# There are multiple ways to choose a pivot, which determines the efficiency of splitting the array into sub-arrays
# The Big-O varies from n*log(n) to n^2, depending on how the pivot is chosen

def partition(array, lowest_index, highest_index):
    # For this implementation, we are using the first element as the pivot
    pivot = array[lowest_index]

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
    return [i - 1, len(array) - 1]

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


input_arr = [4,5,2,3,1] 
count = quick_sort(input_arr, 0, len(input_arr) - 1)
print(input_arr)
print(count)