import sys
sys.stdin=open('input.txt','r')

n = int(input())
d = [0]*1000

d[1]=1
d[2]=3

for i in range(3,n+1):
    d[i] = d[i-1] + (2*d[n-2])

print(d[n]%796796)