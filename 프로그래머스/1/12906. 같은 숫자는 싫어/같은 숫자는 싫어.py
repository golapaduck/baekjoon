def solution(arr):
    answer = [arr[0]]
    for data in arr:
        if answer[-1] == data:
            continue
        else:
            answer.append(data)
    
    return answer