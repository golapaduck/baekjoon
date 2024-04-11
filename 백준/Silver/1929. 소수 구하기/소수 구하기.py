def cal(num):
    for t in range(2,int(num**0.5)+1):
        if num%t==0:
            return False
    return True

n,m = map(int,input().split())

for num in range(n,m+1):
    if num==1:
        continue
    if cal(num):
        print(num)