n = 1260
coin = [500,100,50,10]
count = 0

for i in coin:
    count += n // i
    n %= i

print(n, count)