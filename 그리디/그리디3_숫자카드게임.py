import sys
sys.stdin=open('input.txt','r')

n, m = map(int,input().split())
cards = []
for i in range(n):
    cards.append(list(map(int,input().split())))
result = []

for i in range(n):
    result.append(min(cards[i]))

print(max(result))
