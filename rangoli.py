# given an integer, N. Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)
def print_rangoli(size):
    import string
    alp = string.ascii_lowercase
    l = []
    for i in range(size):
        s = "-".join(alp[i:size])
        l.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print("\n".join(l[:0:-1]+l))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)