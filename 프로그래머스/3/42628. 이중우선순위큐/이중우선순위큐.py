def solution(operations):
    buffer = []
    for operation in operations:
        command, data = operation.split()
        if command == 'I':
            buffer.append(int(data))
            buffer.sort()
        elif command == 'D':
            if data == "-1":
                try:
                    buffer.pop(0)
                except:
                    pass
            elif data == "1":
                try:
                    buffer.pop()
                except:
                    pass
    if len(buffer) == 0:
        return ([0,0])
    else:
        return ([buffer[-1],buffer[0]])