cng = int(input())
cng = 1000-cng
mons = [500,100,50,10,5,1]

ans = 0
for mon in mons:
    if mon <= cng:
        cnt = cng//mon
        ans += cnt
        cng -= mon*cnt

print(ans)