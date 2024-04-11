cro=["c=","c-","dz=","d-","lj","nj","s=","z="]
s=str(input())
for i in cro:
    s=s.replace(i,'*')
print(len(s))