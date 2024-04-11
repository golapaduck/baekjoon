a, b = input().split()

a=int(a)
b=int(b)

if b>=45:
    b=b-45
elif a>0:
    a=a-1
    b=15+b
else :
    a=23
    b=15+b
print(a,b)

