t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    d=y-x
    count=0
    i=1
    n=1
    ans=1
    while(i<d):
        if(count==1):
            n+=1            
            i+=n
            count=0
        else:
            i+=n
            count=1
        ans+=1
    print(ans)
    