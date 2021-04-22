import sys
sys.stdin=open('input.txt','r')

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

for a in lst:
    rank = 1
    for b in lst:
        if a[0]!=b[0] and a[1]!=b[1]:
            if a[0]<b[0] and a[1]<b[1]:
                rank+=1
    print(rank, end=' ')

