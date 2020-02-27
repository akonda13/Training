#!/bin/python

import sys

def minimumSwaps(arr):
    temp = [0] * (len(arr) + 1)
    print(temp)

    for pos, val in enumerate(arr):
        print("pos:", pos, "val:", val)
        temp[val] = pos
        pos += 1

    swaps = 0
    for i in range(len(arr)):
        print("before-loop: ", arr)
        if arr[i] != i+1:
            print("before-temp: ", temp)
            print("before-arr: ", arr)
            swaps += 1
            t = arr[i]       #t=1
            arr[i] = i+1     #1
            arr[temp[i+1]] = t
            temp[t] = temp[i+1]
            print("after-temp: ", temp)
            print("after-arr: ", arr)
            print("========")

    return swaps


fptr = open("inputFile.txt", "r")
line1 = fptr.readline();

n = int(line1.strip())
arr = list(map(int,fptr.readline().strip().split()))
res = minimumSwaps(arr)
print(res)


