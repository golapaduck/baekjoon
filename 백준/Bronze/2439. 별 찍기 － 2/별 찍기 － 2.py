def star(i,count):
    a=""
    for j in range(1,i+1):
        a=a+'*'
    return (f'{a:>{count}}')

T = int(input())

for i in range(1,T+1):
    print(star(i,T))
