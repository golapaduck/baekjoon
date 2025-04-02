from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [0 for _ in range(n)]
    
    for index in range(n):
        if visited[index] == 0:
            dfs(index,visited,computers)
            answer+=1
    
    return answer

def dfs(index,visited,computers):
    visited[index] = 1
    
    for connect in range(len(computers)):
        if connect != index and computers[index][connect] == 1 and visited[connect] == 0:
            dfs(connect,visited,computers)
