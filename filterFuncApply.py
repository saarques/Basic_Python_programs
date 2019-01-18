# In this program, we are going to apply the filter function.

n = (3, 6, 1, 9, 7, 2, 3 ,4)

result = tuple(filter(lambda x: x>=4, n))
print(result)