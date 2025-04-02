def solution(sizes):
    maxW = 0
    maxH = 0
    for i,j in sizes:
        if maxW < max(i,j):
            maxW = max(i,j)
        if maxH < min(i,j):
            maxH = min(i,j)
    return (maxH*maxW)