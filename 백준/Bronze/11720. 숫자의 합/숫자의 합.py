import math

a=int(input())
num=int(input())
sum=0
for i in range(0,a):
    if(i==a-1):
        sum=sum+int(num/10**i)
    elif(i==0):
        sum=sum+int(num%10)
    else:
        sum=sum+int((num%10**(i+1))/(10**i))
print(sum)