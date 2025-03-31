def solution(triangle):

    temp = triangle
    
    for i in range(len(triangle)):
        for j in range(i+2):
            if i == 0:
                temp[i+1][j] += temp[i][0]
            elif i < len(triangle)-1:
                if j == 0:
                    temp[i+1][j] += temp[i][0]
                elif j == i+1:
                    temp[i+1][j] += temp[i][i]
                else:
                    temp[i+1][j] += max(temp[i][j],temp[i][j-1])
    return max(temp[-1])