ts,ps = [0],[0]
n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    ts.append(a)
    ps.append(b)
ts.append(0)
ps.append(0)
dp = [0]*(n+2)
for i in range(n, 0, -1):
    if i + ts[i] > n+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], ps[i] + dp[i+ts[i]])

print(dp[1])