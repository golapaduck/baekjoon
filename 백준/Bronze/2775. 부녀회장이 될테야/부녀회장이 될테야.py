
t=int(input())
for i in range(t):
    k=int(input())
    n=int(input())
    f=[x for x in range(1,n+1)]
    for k in range(k):
        for i in range(1,n):
            f[i] += f[i-1]
    print(f[-1])