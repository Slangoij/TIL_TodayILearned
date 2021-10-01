n = int(input())
dp = [1 for i in range(n)]
for i in range(1, n-1):
    dp[i+1] = dp[i] + dp[i-1]
print(dp[-1])