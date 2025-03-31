def solution(citations):
    answer = 0
    citations = sorted(citations,reverse=True)
    
    for num in range(len(citations)):
        if citations[num] >= num +1:
            answer = num+1
            
    return answer

# [0, 1, 3, 4, 5, 6]