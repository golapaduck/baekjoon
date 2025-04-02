def solution(jobs):
    start = [i for i,_ in jobs]
    ready = []
    result = []
    
    timer = 0
    processTime = 0
    
    while len(result) < len(jobs):
        
        if start.count(timer) > 0:
            startIndex = 0
            for _ in range(start.count(timer)):
                nextIndex = start.index(timer,startIndex)
                ready.append([nextIndex] + jobs[nextIndex])
                startIndex = nextIndex+1
            ready = sorted(ready, key=lambda x: (x[2],x[1],x[0]))

        if timer >= processTime:
            try:
                data = ready.pop(0)
                processTime = timer+data[2]
                result.append(processTime-data[1])
            except:
                pass
        timer += 1
    
    return int(sum(result)/len(result))