n,k = map(int, input().split())
dp = [0]*(k+1)
coins = []
for _ in range(n):
    coins.append(int(input()))
for i in range(2,k+1):
    for j in range(i-1,(i-1)//2,-1):
        if dp[i-j]:
            dp[i] += dp[j]
