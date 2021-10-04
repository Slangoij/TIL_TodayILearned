crdprc = [0]
n = int(input())
crdprc += list(map(int, input().split()))
dp = [0]
for i in range(1,n+1):
    tmpmax = 0
    for j in range(1,i):
        tmpmax = max(tmpmax, dp[j]+crdprc[i-j])
    tmpmax = max(tmpmax, crdprc[i])
    dp.append(tmpmax)
print(dp[n])