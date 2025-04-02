from collections import deque

def bfs(start, end, visited, graph):
    visited[start] = 1
    visited[end] = 1
    q = deque()
    q.append(end)
    cnt = 1
    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = 1
                cnt+=1
                q.append(next)
    return cnt

def solution(n, wires):
    answer = int(1e9)
    graph = [[] for _ in range(n+1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    for start, end in wires:
        visited = [0 for _ in range(n+1)]
        
        cnt = bfs(start,end,visited,graph)
        other_cnt = abs(n-cnt)
        
        answer = min(answer,abs(cnt-other_cnt))
        
    return answer
    