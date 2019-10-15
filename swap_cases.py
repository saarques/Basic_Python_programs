# Swap cases in a string
def swap_case(s):
    a = []
    for i in range(len(s)):
        if s[i] == s[i].lower():
            a.append(s[i].upper())
        else:
            a.append(s[i].lower())
    return "".join(a)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)