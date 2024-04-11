def p(num):
    if (num>1):
        return p(num-1)+p(num-2)
    elif(num==1):
        return 1
    elif(num==0):
        return 0


b=int(input())

print(p(b))