def solution(clothes):
    dict = {}
    for _, category in clothes:
        try:
            dict[category] = dict[category] + 1
        except:
            dict[category] = 1
            
    answer = 1
    
    for count in dict.values():
        answer *= count+1
    
    answer -= 1
    
    return answer