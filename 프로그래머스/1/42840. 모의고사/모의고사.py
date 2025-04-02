def solution(answers):
    score = [0,0,0]
    
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        answer = answers[i]
        
        if a[i%5] == answer:
            score[0] += 1
        if b[i%8] == answer:
            score[1] += 1
        if c[i%10] == answer:
            score[2] += 1
    
    result = []
    start=0
    for _ in range(score.count(max(score))):
        index = score.index(max(score),start)
        result.append(index+1)
        start = index+1
    
    result.sort()
    
    return result