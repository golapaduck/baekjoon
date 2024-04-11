s=str(input()).upper()
a=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
count=list()
num=0
char=''
for i in a:
    count.append(s.count(i))
    if(s.count(i)>num):
        num=s.count(i)
        char=i
        
if(count.count(num)>=2):
    print('?')
else:
    print(char)