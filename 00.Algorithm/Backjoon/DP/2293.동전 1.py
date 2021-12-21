import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (k+1)
dp[0] = 1
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort()
# for i in range(1, k+1):
#     # for j in range(i-1, (i-1)//2, -1):
#     #     if dp[j] != 0 and i-j in coins:
#     #         dp[i] += dp[j]
#     for j in range(1, i//2+1):
#         if dp[j] and i-j in coins:
#             dp[i] += dp[j]
#     if i in coins:
#         dp[i] += 1
# print(dp[-1])

for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]
print(dp[k])
