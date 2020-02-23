#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
#def rotLeft(a, d):

def array_left_rotation(a, k):
    return a[k:] + a[:k]
    # print(a[k:])
    #print(a[:k])

fptr = open("inputFile.txt", "r")
line1 = fptr.readline();

line2 = fptr.readline();

n, k = map(int, line1.strip().split(' '))
#a = list(map(int, line2.rstrip().split()))
a = list(line2.rstrip().split(' '))

print(a)

answer = array_left_rotation(a, k);
# print (' '.join(map(str,answer)))
print (' '.join(answer))
