import sys
sys.stdin=open('input.txt','r')

n = []
A, B, C = map(int, input().split())
for i in range(3):
    n.append(list(map(int,input().split())))
max = 0
for i in range(len(n)):
    for j in range(0,2):
        if n[i][j] > max:
            max = n[i][j]
board = [0]*(max-1)

for i in n:
    for j in range(i[0]-1, i[1]-1):
        board[j] = board[j]+1
result = 0

for i in range(len(board)):
    if board[i] == 1:
        result += A
    elif board[i] == 2:
        result += 2*B
    else: result += 3*C

print(result)
