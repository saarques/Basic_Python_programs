# Consider a list (list = []). You can perform the following 
# commands:

# insert i e: Insert integer 

# at position i
# print: Print the list.
# remove e: Delete the first occurrence of integer e
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
if __name__ == '__main__':
    N = int(input())
    a =[]
    b = []
    for _ in range(N):
        a.append(str(input()).split(" "))
    for index in range(len(a)):
        if a[index][0] == "insert":
            b.insert(int(a[index][1]), int(a[index][2]))
        if a[index][0] == "remove":
            b.remove(int(a[index][1]))
        if a[index][0] == "sort":
            b = sorted(b)
        if a[index][0] == "append":
            b.append(int(a[index][1]))
        if a[index][0] == "pop":
            b.pop()
        if a[index][0] == "reverse":
            b.reverse()
        if a[index][0] == "print":
            print(b)