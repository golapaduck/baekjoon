def star(i):
    a=""
    for j in range(1,i+1):
        a=a+'*'
    return a

T = int(input())

for i in range(1,T+1):
    print(star(i))