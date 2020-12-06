# Merge sort - used for sorting an array of n integers
# Has a Big-O of nlog(n)
def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            first = left.pop(0)
            result.append(first)
        else:
            first = right.pop(0)
            result.append(first)

    while len(left) > 0:
        item = left.pop(0)
        result.append(item)

    while len(right) > 0:
        item = right.pop(0)
        result.append(item)

    return result

def merge_sort(array):
    # if array is length 1 or less, return the array
    if  len(array) <= 1:
        return array

    else:
    # else split it into two equal sized arrays
        n = len(array)
        nBy2 = n // 2
        a = array[0:nBy2]
        b = array[nBy2:n]

    # apply merge sort to each sub array
        left = merge_sort(a)
        right = merge_sort(b)

    # return the merged results
        return merge(left, right)

x = [456,2,4,8,99,5,12,5,90,55432,1,6]
print(merge_sort(x))