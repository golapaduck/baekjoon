def solution(money):
    dp1 = [0 for _ in range(len(money))]
    dp2 = [0 for _ in range(len(money))]
    
    for i in range(len(money)-1):
        if i == 0:
            dp1[0] = money[0]
        elif i == 1:
            dp1[1] = max(dp1[0],money[1])
        else:
            dp1[i]=max(dp1[i-1],dp1[i-2]+money[i])
        
    for i in range(len(money)):
        if i == 0:
            dp2[i] = 0
        elif i == 1:
            dp2[i] = money[i]
        else:
            dp2[i]=max(dp2[i-1],dp2[i-2]+money[i])
    
    return (max(max(dp1),max(dp2)))
    
# [0,0,0,0,0,0]