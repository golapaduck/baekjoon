def solution(priorities, location):
    count = 1
    while len(priorities) > 0:
        maxNum = max(priorities)
        for _ in range(len(priorities)):
            data = priorities.pop(0)
            if data == maxNum:
                if location == 0:
                    return count
                else:
                    location -= 1
                    count += 1
                    break
            else:
                priorities.append(data)
                location -= 1
                if location < 0:
                    location += len(priorities)