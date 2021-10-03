dp = [[1,0],[1,2]]
n = int(input())
for i in range(3,n+1):
    dp.append([sum(dp[i-2]), dp[i-3][0]*2])
print(sum(dp[n-1]))