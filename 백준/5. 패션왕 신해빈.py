import sys
sys.stdin=open('input.txt','r')

t = int(input())
for _ in range(t):
    n = int(input())
    dict = {}
    for i in range(n):
        a, b = map(str, input().split())

        if b not in dict.keys():
            dict[b] = 1
        else:
            dict[b] += 1
    result = 1
    for value in dict.values():
        result = result * (value+1)
    print(result-1)
