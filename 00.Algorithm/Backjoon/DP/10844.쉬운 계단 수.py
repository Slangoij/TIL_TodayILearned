n = int(input())
dp = [[0,1,1,1,1,1,1,1,1,1]]
for i in range(n-1):
    tmp = []
    for j in range(10):
        if j == 0:
            tmp.append(dp[i][1])
        elif j == 9:
            tmp.append(dp[i][8])
        else:
            tmp.append(dp[i][j-1] + dp[i][j+1])
    dp.append(tmp)
print(sum(dp[-1])%1000000000)