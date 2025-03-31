def solution(m, n, puddles):
    check = [[0 for _ in range(n)] for _ in range(m)]
    
    for x in puddles:
        check[x[0]-1][x[1]-1] = "x"

    check[0][0]=1
    
    for i in range(m):
        for j in range(n):
            if check[i][j] != "x":
                count = check[i][j]
                if i > 0 and check[i-1][j] != "x":
                        count += check[i-1][j]
                if j > 0 and check[i][j-1] != "x":
                        count += check[i][j-1]
                check[i][j] = count % 1000000007

    return check[m-1][n-1]