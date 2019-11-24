# Raghu is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay x

# amount of money only if they get the shoe of their desired size.

# Your task is to compute how much money Raghu earned.


import sys
from collections import Counter
n = int(sys.stdin.readline())
shoe = Counter(map(int, sys.stdin.readline().split(" ")))
l = int(sys.stdin.readline())
sum = 0
for i in range(l):
    f, g = (map(int, sys.stdin.readline().split(" ")))
    if shoe[f]:
        sum += g
        shoe[f] = shoe[f] - 1
print(sum)