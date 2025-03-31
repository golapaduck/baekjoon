def solution(N, number):
    answer = -1
    
    if N == number:
        return 1
    
    check = [set() for i in range(8)]
    
    for i in range(len(check)):
        check[i].add(int(str(N)*(i+1)))   
    
    for i in range(1,8):
        for j in range(i):
            for op1 in check[j]:
                for op2 in check[i-j-1]:
                    check[i].add(op1+op2)
                    check[i].add(op1-op2)
                    check[i].add(op1*op2)
                    if op2 != 0:
                        check[i].add(op1//op2)
        if number in check[i]:
            answer = i+1
            break
    return answer
    