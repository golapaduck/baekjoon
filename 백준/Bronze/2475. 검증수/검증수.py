number = list(map(int,input().split()))
cache = 0
for index in number:
    cache += index * index
verification = cache % 10
print(verification)