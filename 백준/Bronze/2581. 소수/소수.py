m = int(input())
n = int(input())

a=list()

for num in range(m,n+1):
    i=2
    while(i<=num):
        if num==i:
            a.append(num)
        if num%i==0:
            break
        i+=1

if len(a)==0:
    print(-1)
    
else:
    print(sum(a))
    print(min(a))