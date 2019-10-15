# Given the names and grades for each student in a Physics 
# class of students, store them in a nested list and print 
# the name(s) of any student(s) having the second lowest grade.
if __name__ == '__main__':
    dictio = {}
    a = []
    for _ in range(int(input())):
        name = str(input())
        score = float(input())
        dictio[name] = score
        a.append(score)

b = sorted(list(set(a)))[1]
a = []
for key in dictio:
    c = dictio.get(key)
    if b == c:
        a.append(key)

a = sorted(a)
for i in a:
    print(i)