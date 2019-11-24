# The first line contains a single string denoting s.
# The second line contains an integer, k, denoting the length of each subsegment.
# Delete duplicates from each subsegment and print them.
def merge_the_tools(string, k):
    t = [string[i:i+k] for i in range(0, len(string), k)]
    for element in t:
        som = [element[i] for i in range(len(element))]
        block = []
        for value in som:
            if value not in block:
                block.append(value)
        print("".join(block))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)