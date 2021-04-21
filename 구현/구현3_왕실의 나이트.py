import sys
sys.stdin=open('input.txt','r')

y = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
input_ = input()
loc = []
for i in input_:
    loc.append(i)
for i in y.keys():
    if i == loc[0]:
        loc[0] = y.get(i)
loc[1] = int(loc[1])

x, y = loc[0], loc[1]
dx = [-2,-2,-1,1,2,2,1,-1]
dy = [-1,1,2,2,1,-1,-2,-2]
count = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx > 0 and ny > 0 and nx < 9 and ny < 9:
        count += 1
print(count)