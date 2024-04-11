def p(num):
    if (num>0):
        return num*p(num-1)
    
    elif(num==0):
        return 1


b=int(input())

print(p(b))