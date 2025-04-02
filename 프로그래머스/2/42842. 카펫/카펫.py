
def solution(brown, yellow):
    sum = (brown/2)+2
    mul = brown+yellow
    
    for i in range(1,int(sum//2)+1):
        if i*(sum-i) == mul:
            return[int(sum-i),i]
