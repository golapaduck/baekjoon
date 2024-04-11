count=int(input())

for i in range(0,count):
    a=list(input().split())
    num=int(a[0])
    s=list(a[1])
    for j in s:
        for k in range(0,num):
            print(j,end="")
    print()