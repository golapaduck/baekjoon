n=int(input())

i=0
ans=-1

if(n%5==0):
    print(int(n/5))
else:
    while(i*5<n):
        num=n-i*5
        if(num%3==0):
            ans=i+num/3
        i+=1
    print(int(ans))
    