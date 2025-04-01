def solution(progresses, speeds):
    INF = int(1e9)
    answer = []
    
    buffer = []
    for i in range(len(progresses)):
        date = (100 - progresses[i])//speeds[i]
        if (100 - progresses[i])%speeds[i]>0:
            date += 1
        buffer.append(date)
        
    print(buffer)
    
    num = 1
    for i in range(len(buffer)):
        if i == 0:
            continue
        elif buffer[i-1] >= buffer[i]:
            num+=1
            buffer[i] = buffer[i-1]
        else:
            answer.append(num)
            num = 1
        if i == len(buffer)-1:
            answer.append(num)
            
        
    return answer

# 	[7, 3, 9]