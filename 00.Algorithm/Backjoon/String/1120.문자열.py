a,b = input().split()
ans = len(a)
for mov in range(len(b)-len(a)+1):
    tmp = 0
    for i in range(len(a)):
        if a[i] != b[i+mov]:
            tmp += 1
    ans = min(ans, tmp)
print(ans)