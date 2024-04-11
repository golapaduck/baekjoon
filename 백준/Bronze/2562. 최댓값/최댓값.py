a=list()
for i in range(1,10):
    a.append(int(input()))

b=list(a)
a.sort()
val=(a.pop())
count=1
temp=0

for i in b:
    if(i==val):
        temp=count
    else:
        count=count+1
print(val)
print(temp)