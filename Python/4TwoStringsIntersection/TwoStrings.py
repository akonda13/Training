#!/bin/python

import sys

def minimumSwaps(s1, s2):
    if (s1.intersection(s2)):
        print('YES')
    else:
        print('NO')



fptr = open("inputFile.txt", "r")
line1 = fptr.readline();

s1 = set(line1.strip())
s2 = set(fptr.readline().strip())
print(s1)
print(s2)
print(s1.intersection(s2))
minimumSwaps(s1, s2)
