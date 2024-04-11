s = list(input().split())
a = list(str(s[0]))
b = list(str(s[1]))
ans = list()
j = 2
while (True):
    if (a[j] > b[j]):
        ans = a
        break
    elif (a[j] < b[j]):
        ans = b
        break
    else:
        if (j == 0):
            ans = a
            break
        j = j-1
print(ans[2]+ans[1]+ans[0])