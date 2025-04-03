from collections import deque

def solution(maps):
    
    q = deque()
    q.append((0,0))
    
    while q:
        x,y = q.popleft()
        
        if (x,y) == (len(maps),len(maps[0])):
            break

        for i in range(-1,2):
            for j in range(-1,2):
                if abs(i+j) == 2 or abs(i+j) == 0:
                    continue
                
                next_x = x + i
                next_y = y + j
                
                if next_x < 0 or next_y < 0 or next_x==len(maps) or next_y == len(maps[0]):
                    continue
                if maps[next_x][next_y] == 0:
                    continue
                if maps[next_x][next_y] == 1:
                    maps[next_x][next_y] = maps[x][y]+1
                
                    q.append((next_x,next_y))
                    
    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]
                
