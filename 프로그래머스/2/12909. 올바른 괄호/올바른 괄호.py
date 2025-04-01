def solution(s):
    
    buffer = []
    for i in s:
        if i == '(':
            buffer.append(i)
        else:
            try:
                buffer.pop()
                continue
            except:
                return False
    if len(buffer):
        return False
    else:
        return True
    
    