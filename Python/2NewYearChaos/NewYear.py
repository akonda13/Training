#!/bin/python

import sys

fptr = open("inputFile.txt", "r")
line1 = fptr.readline();

T = int(line1.strip())
for a0 in range(T):
    n = int(fptr.readline().strip())
    q = list(map(int,fptr.readline().strip().split(' ')))
    print(q)

    # your code goes here
    b = {}
    r = 0
    cont = True
    while cont:
        cont = False
        for i in range(n-1):
            if q[i] > q[i+1]:
                if not q[i] in b:
                    b[q[i]] = 0
                    print(i, "===",b)
                b[q[i]] += 1
                print(i, "===",b)
                print(i, "===", q)

                if b[q[i]] > 2:
                    cont = False
                    r = "Too chaotic"
                    break

                q[i], q[i+1] = q[i+1], q[i]
                print(i, "===", q)

                r += 1
                cont = True
    print(r)
