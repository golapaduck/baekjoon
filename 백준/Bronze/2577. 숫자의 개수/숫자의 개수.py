a=int(input())
b=int(input())
c=int(input())

ans=str(a*b*c)

for i in range(0,10):
    print(ans.count(str(i)))