num=[" ","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
a=list(str(input()))
time=0

for i in a:
    count=0
    while(count<len(num)):
        if(num[count].find(i)!=-1):
            time=time+count+2
            break
        else:
            count=count+1
print(time)
            