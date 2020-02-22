#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
#def rotLeft(a, d):

def array_left_rotation(a, n, k):
    return a[k:] + a[:k]

fptr = open("inputFile.txt", "r")
line1 = fptr.readline();

line2 = fptr.readline();

n, k = map(int, line1.strip().split(' '))
a = list(map(int, line2.rstrip().split()))

answer = array_left_rotation(a, n, k);
print (' '.join(map(str,answer)))



'''
nd = line1.split()

n = int(nd[0])

d = int(nd[1])
print(d)

b = line2.split()

a = list(map(int, line2.rstrip().split()))
print(a)

newList = []
for x in range(1,d+1):
    newList[x] = a[x+1]

print(newList)

fptr.close()
'''
'''
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
'''
