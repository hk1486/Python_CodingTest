import sys
sys.stdin=open('input.txt','r')

n = int(input())
directions = input().split()
x, y = 1, 1
dx = [-1,0,1,0]
dy = [0,1,0,-1]
move = ['U','R','D','L']

for direction in directions:
    for i in range(4):
        if direction == move[i]:
            new_x = x + dx[i]
            new_y = y + dy[i]
    if new_x < 1 or new_y < 1 or new_x > n or new_y > n:
        continue
    x = new_x
    y = new_y
print(x,y)