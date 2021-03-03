import sys
sys.stdin=open('input.txt','r')

n = int(input())
lst = list(map(int,input().split()))
lst.sort(reverse=True)
count = 0

for i in lst:
    if len(lst) >= i:
        lst = lst[i:]
        count += 1

print(n, lst, count)