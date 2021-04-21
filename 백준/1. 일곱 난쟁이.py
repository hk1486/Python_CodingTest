import sys
sys.stdin=open('input.txt','r')

n = []
[n.append(int(input())) for i in range(9)]
n.sort()
result = sum(n)
for i in range(9):
    for j in range(i+1,9):
        if result - n[i] - n[j] == 100:
            for k in range(9):
                if k!=i and k!=j:
                    print(n[k])
            exit()