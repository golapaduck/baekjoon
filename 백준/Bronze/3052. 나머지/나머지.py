a=list()
b=list()

for i in range(0,10):
    a.append(int(input()))
    
for i in a:
    if(b.count(i%42)==1):
        continue
    b.append(i%42)
print(len(b))