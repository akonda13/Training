#!/bin/python

import sys

def number_needed(a, b):
    H = {}
    count = 0
    for i in range(len(a)):
        if not H[a[i]]:
            H[a[i]] = 1
        else:
            H[a[i]] += 1

    for i in range(len(b)):
        if H[b[i]]:
            H[b[i]] -= 1
        else:
            count += 1
    for v in H.values():
        count += v
    return count



fptr = open("inputFile.txt", "r")
line1 = fptr.readline();

s1 = set(line1.strip())
s2 = set(fptr.readline().strip())
print(s1)
print(s2)
print(number_needed(s1, s2))
