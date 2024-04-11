count, val = input().split()
count = int(count)
val = int(val)

a=[]
a=list(map(int,input().split()))

for i in a:
    if(i<val):
        print(i, end=' ')