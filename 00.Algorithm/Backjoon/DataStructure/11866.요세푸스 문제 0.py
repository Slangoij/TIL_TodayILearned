n, k = map(int, input().split())
lst = [str(i) for i in range(1,n+1)]
ans = []
idx = k-1
while True:
    ans.append(lst.pop(idx))
    if lst:
        idx = (idx+k-1) % len(lst)
    else:
        break
print('<'+", ".join(ans)+'>')