def dec(num):
    i=2
    while(i<=num):
        if num%i==0:
            print(i)
            dec(int(num/i))
            break
        i+=1
    return 0

num=int(input())

dec(num)

