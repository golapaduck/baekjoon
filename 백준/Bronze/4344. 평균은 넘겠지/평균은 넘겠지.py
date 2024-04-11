count=int(input())
stu=list()

for i in range(0,count):
    a=list(map(int,input().split()))
    a.reverse()
    stu.append(a)

for i in stu:
    num=i.pop()
    total=0
    for j in i:
        total=total+j
    avr=total/num
    total=0
    for j in i:
        if(j>avr):
            total=total+1
    print(f'{total/num*100:.3f}%')