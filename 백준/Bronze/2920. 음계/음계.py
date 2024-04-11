tone = list(map(int, input().split()))
sort = sorted(tone)
if (sort == tone):
    print("ascending")
elif (list(reversed(sort)) == tone):
    print("descending")
else:
    print("mixed")
