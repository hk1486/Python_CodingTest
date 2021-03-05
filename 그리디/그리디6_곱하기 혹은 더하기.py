import sys
sys.stdin=open('input.txt','r')

n = input()
a = []
for i in n:
    a.append(int(i))
a.sort()
result = 0

for i in range(len(a)):
    if a[i] == 1 or a[i] == 0:
        result += a[i]
    elif result != 0 and a[i-1] != 1 and a[i-1] != 0:
        result *= a[i]
    else:
        result += a[i]

print(n, a, result) 