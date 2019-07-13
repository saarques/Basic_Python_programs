import sys

def find_freq_bef_occurence(string, n):
	character = string[n - 1]
	return string[:n-1].count(character) 

N = int(sys.stdin.readline())

string = sys.stdin.readline()

Q = int(sys.stdin.readline())

for index in range(Q):
	n = (int(sys.stdin.readline()))
	print(find_freq_bef_occurence(string, n))