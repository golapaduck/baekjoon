val=int(input())
count=0
check=val
temp=0
ch=0

while True:
    count=count+1
    temp=val//10+val%10
    ch=(val%10)*10+temp%10
    val=ch
    if(val==check):
        break
print(count)
