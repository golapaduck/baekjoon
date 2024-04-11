c=int(input())
count=0
for i in range(0,c):
    s=str(input())
    error=0
    for j in range(0,len(s)-1):
        if(s[j]!=s[j+1]):
            n=s[j+1:]
            if(n.count(s[j])!=0):
                error=error+1
    if error==0:
        count += 1
print(count)
                