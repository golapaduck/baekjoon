T = int(input())
case=[]

for i in range(1,T+1):
    a,b=input().split()
    a=int(a)
    b=int(b)
    case.append([a,b])
    
for i in range(0,T):
    print(case[i][0]+case[i][1])
    