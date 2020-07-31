# Highest Magic number, where magic number is a number whose left number is greater than the sum of the left numbers

# Input ends with 0

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
p=[]
while True:
    xx=input()
    if xx=='0':break
    x = list(map(int,xx))
    m=True
    for i in range(len(x)-1):
        if x[i]<=sum(x[i+1:]): m=False
    if m:p+=[int(xx)]
print('NONE' if len(p)==0 else max(p))