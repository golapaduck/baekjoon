#2210
result = set()
board = [list(map(str, input().split())) for _ in range(5)]
d = [(-1,0), (1,0), (0,-1), (0,1)]

def dfs(x,y,num):
    if len(num) == 6:
        result.add(num)
        return
    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if (0 <= ny < 5) and (0 <= nx < 5):
            dfs(nx, ny, num + board[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i,j,board[i][j])

print(len(result))