arr = [1,3,5,7,4,6,8,9,2]

def merge_sort(array):
    # if array is length 1 or less, return the array
    if  len(array) <= 1:
        return array

    else:
    # else split it into two equal sized arrays
        n = len(array)
        nBy2 = n // 2
        sub_arr_1 = arr[0:nBy2]
        sub_arr_2 = arr[nBy2:n]

    # apply merge_sort to each sub array
        a = merge_sort(sub_arr_1)
        b = merge_sort(sub_arr_2)

    # merge the results by looping through the two arrays
        i=0
        j=0

        result = []

        for k in range(0,n):  
            if i >= len(a):
                result.append(b[j])
                j+=1

            elif j >= len(b):
                result.append(a[i])
                i+=1

            elif a[i] < b[j]:
                result.append(a[i])
                i+=1

            else:
                result.append(b[j])
                j+=1
        
        return result

print(merge_sort(arr))