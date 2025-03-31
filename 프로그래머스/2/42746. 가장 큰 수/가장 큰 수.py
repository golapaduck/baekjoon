def solution(numbers):
    answer = ''
    numbers = sorted(numbers, key=lambda x: str(x)*3)
    
    for _ in range(len(numbers)):
        number = numbers.pop()
        answer += str(number)
        
    return answer if int(answer) != 0 else '0'