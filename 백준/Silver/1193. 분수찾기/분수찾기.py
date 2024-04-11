a=int(input())
num=1
total=1

while(a>total):
    num+=1
    total+=num

if(num%2==0):
    print("%d/%d"%(a-total+num,1-a+total))
else:
    print("%d/%d"%(1-a+total,a-total+num))
