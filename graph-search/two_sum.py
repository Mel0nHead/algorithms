file = open("./two_sum_data.txt","r")

array = sorted([int(i) for i in file])
lowerBound = -10000
upperBound = 10000

i = 0
j = len(array) - 1
H = {} # this could be a set

while i < j:
    print(j - i)
    if array[i] + array[j] < lowerBound:
        i += 1
    elif array[i] + array[j] > upperBound:
        j -= 1
    else:
        for x in range(i,j):
            numX = array[x]
            numJ = array[j]

            if numX + numJ > upperBound:
                break
            else:
                if numX != numJ:
                    H[numX + numJ] = 1
              
        j -= 1 # might be dodgy, not sure

print(len(H.keys()))
# FIND t in [3,10]
# should get 3, 4, 5, 6, 7, 8, 9, 10
# [-2, 0, 0, 4]

# i = 0, j = 8: sum = 8; iterate through range(i,j) finding 8, 10, 12 (then break and j--)
# i = 0, j = 7: sum = 6; iterate through range(i,j) finding 6, 8, 10, 11 (then break and j--)
# i = 0, j = 6: sum = 4; iterate through range(i,j) finding 4, 6, 8, 9, 9, 13 (then break and j--)
# i = 0, j = 5: sum = 3; iterate through range(i,j) finding 3, 5, 7, 8, 8 (come to end of loop, so i++)
# i = 1, j = 5: sum = 5; iterate through range(i,j) finding 5, 7, 8, 8 (come to end of loop, so i++)
# i = 2, j = 5: sum = 7; iterate through range(i,j) finding 7, 8, 8 (come to end of loop), so i ++