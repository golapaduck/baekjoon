import sys

input = sys.stdin.readline
print = sys.stdout.write

MAX = 1000000
arr = [0] * (MAX+1)

for i in range(2,MAX+1):
    buffer = 0
    for j in range(i,MAX+1):
        buffer += j
        if(buffer > MAX):
            break
        else:
            arr[buffer] += 1

while True:
    price = int(input())
    if price == 0:
        exit()
    print("%d\n" %arr[price])