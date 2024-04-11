count=int(input())
a=list()

for i in range(0,count):
    a.append(input())

temp='X'

for i in a:
    count=1
    score=0
    for j in i:
        if(j=='O'):
            if(temp=='O'):
                count=count+1
                score=score+count
            else:
                score=score+1
                count=1
        temp=j
    temp='X'
    print(score)