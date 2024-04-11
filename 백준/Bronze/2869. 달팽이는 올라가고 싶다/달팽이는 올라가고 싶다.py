import math
s=list(map(int,input().split()))
a=s[0]
b=s[1]
v=s[2]

print(math.ceil((v-b)/(a-b)))