def solution(arr):
    INF = int(1e9)
    
    calcData = []
    numData = []
    
    for index in range(len(arr)):
        if index%2 == 1:
            calcData.append(arr[index])
        else:
            numData.append(int(arr[index]))
    
    n = len(numData)
    
    MAX_DP = [[-INF for _ in range(n)] for _ in range(n)]
    MIN_DP = [[INF for _ in range(n)] for _ in range(n)]
    #   i=시작, j는 끝
    for step in range(n):
        for i in range(n-step):
            j = i + step
            
            if step == 0:
                MAX_DP[i][i] = numData[i]
                MIN_DP[i][i] = numData[i]
            else:
                for k in range(i,j):
                    # print(f"step: {step},i: {i},j: {j},k: {k}")
                    if calcData[k] == '+':
                        MAX_DP[i][j] = max(MAX_DP[i][j],MAX_DP[i][k] + MAX_DP[k+1][j])
                        MIN_DP[i][j] = min(MIN_DP[i][j],MIN_DP[i][k] + MIN_DP[k+1][j])
                    else:
                        MAX_DP[i][j] = max(MAX_DP[i][j],MAX_DP[i][k] - MIN_DP[k+1][j])
                        MIN_DP[i][j] = min(MIN_DP[i][j],MIN_DP[i][k] - MAX_DP[k+1][j])
    
    return MAX_DP[0][n-1]
                            