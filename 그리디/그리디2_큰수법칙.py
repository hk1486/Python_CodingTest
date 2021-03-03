import sys
sys.stdin=open('input.txt','r')
n, m, k = map(int,input().split())
lst = list(map(int,input().split()))
result = 0

lst.sort(reverse=True)
first = lst[0]
second = lst[1]

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1

    if m == 0:
        break
    result += second
    m -= 1

print(n,m,k,lst)
print(result)
