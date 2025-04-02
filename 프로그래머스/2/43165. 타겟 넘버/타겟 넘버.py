def dfs(temp,start,target,numbers):
    
    sumTemp = temp + numbers[start]
    subTemp = temp - numbers[start]
    
    if start == len(numbers)-1:
        count = 0
        if sumTemp == target:
            count+=1
        if subTemp == target:
            count+=1

            
        return count
    else:
        sumCount = dfs(sumTemp,start+1,target,numbers)
        subCount = dfs(subTemp,start+1,target,numbers)
        
        return sumCount + subCount
        
    
    
def solution(numbers, target):
    start = 0
    temp = 0
    
    return dfs(temp,start,target,numbers)