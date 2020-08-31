#!/bin/python

import sys

def diagonalDifference(arr):

    left_to_right = 0
    right_to_left = 0

    rows = len(arr)
    columns = len(arr[0])

    i = 0
    j = 0
    k = 0
    l = rows - 1

    while (i < rows and j < columns and k < rows and l >= 0 ):
        left_to_right += arr[i][j]
        right_to_left += arr[k][l]
        i += 1
        j += 1
        k += 1
        l -= 1

    print (left_to_right)
    print (right_to_left)

    return abs(left_to_right - right_to_left)


fptr = open("inputFile.txt", "r")

n = int(fptr.readline().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, fptr.readline().rstrip().split())))


print(n)  # 3
print(arr) # [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

result = diagonalDifference(arr)
print (result)



