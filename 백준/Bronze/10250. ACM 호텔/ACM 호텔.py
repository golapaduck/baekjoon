t=int(input())
for i in range(0,t):
    s=list(map(int,input().split()))
    h=s[0]
    w=s[1]
    n=s[2]
    
    if(n%h==0):
        first=h*100
        last=int(n/h)
    else:
        first=n%h*100
        last=int(n/h+1)
    print(first+last)