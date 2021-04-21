import sys
sys.stdin=open('input.txt','r')

s = input()
b = []
for i in range(len(s)):
    if s[i] == s[-(i+1)]:
        b.append(s[i])
    if s[i] != s[-(i+1)]:
        if s[i] < s[-(i+1)]:
            b.append(s[-(i+1)])
        else:
            b.append(s[i])
for i in range(len(b)):
    print(b[i], end='')