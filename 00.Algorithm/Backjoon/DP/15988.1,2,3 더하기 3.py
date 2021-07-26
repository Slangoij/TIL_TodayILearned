T = int(input())
to_do = []
for _ in range(T):
    to_do.append(int(input()))

dp = [0]*1000001
dp[1] = 1
dp[2] = 2
dp[3] = 4
max_val = max(to_do)
for i in range(4, max_val+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009

for now in to_do:
    print(dp[now])