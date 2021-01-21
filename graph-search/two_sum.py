file = open("./two_sum.txt","r")

array = sorted([int(i) for i in file])
lowerBound = 3
upperBound = 10

i = 0
j = len(array) - 1
H = {}

while i < j:
    if array[i] + array[j] < lowerBound:
        i += 1
    elif array[i] + array[j] > upperBound:
        j -= 1
    else:
        for x in range(i,j):
            if array[x] + array[j] > upperBound:
                j -= 1
                break
            else:
                if x != j:
                    H[x + j] = 1
        i += 1





