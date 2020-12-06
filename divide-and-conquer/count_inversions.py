# Algorithm for counting the number of inversions in an array - done by extending the merge sort algorithm
# Inversion is defined as a pair with indices (i,j) in array A such that i < j and A[i] > A[j]
# Has a Big-O of nlog(n)
def merge_and_count_split_inversions(left, right):
    result = []
    inversion_count = 0

    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            first = left.pop(0)
            result.append(first)
        else:
            # If the first item in the right hand array is less than the first item in the left array, then 
            # it must also be less than all the other remaining items in the left hand array, since both arrays 
            # are sorted in ascending order.
            inversion_count += len(left)
            first = right.pop(0)
            result.append(first)

    while len(left) > 0:
        item = left.pop(0)
        result.append(item)

    while len(right) > 0:
        item = right.pop(0)
        result.append(item)

    return [result, inversion_count]


def sort_and_count_inversions(array):
    # an array of one or less items cannot have any inversions
    if len(array) <= 1:
        return [array, 0]

    else:
        # split array into two equal sized arrays
        n = len(array)
        nBy2 = n // 2
        a = array[0:nBy2]
        b = array[nBy2:n]

        # sort and count the number of inversions in both subarrays
        [left, left_inversions] = sort_and_count_inversions(a)
        [right, right_inversions] = sort_and_count_inversions(b)
        # count the number of split inversions in the original array
        [sorted_array, split_inversions] = merge_and_count_split_inversions(left, right)

        return [sorted_array, left_inversions + right_inversions + split_inversions]

print(sort_and_count_inversions([6,5,4,3,2,1])[1])