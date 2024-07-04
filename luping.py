
import math
b = 9
for j in range (b):
    for i in range(b):
        print(j,i,"I",end=" ")
    print(" ")

a = 11
for y in range(a):
    for u in range(a):
        if y == round(a / 2) - 1 or u == round(a / 2)- 1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print(" ")

for j in range(b):
    for i in range(b):
        if (j == i or j+i == b-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        print(" ")
    for j in range(b):
        for i in range(b):
            if (j == i or j + i == b - 1
                    or j ==math.ceil(b/2)-1
                    or i == math.ceil(b/2)-1
                    or i == 0
                    or i == b-1
                    or j == 0
                    or j == b-1):
                print("*",end=" ")
            else:
               print(" ", end=" ")
        print("")

import math
b = 5
for j in range(b):
    for i in range(b):
        print(" o ",end=" ")
    print(" ")

for j in range(b):
    for i in range(j+1):
        print("  o  ", end=" ")
    print(" ")

c = 5
for j in range(c):
    for i in range(c):
        if (j >= c-i-1):
            print("o",end=" ")
    print(" ")


