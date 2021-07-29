n, k = map(int, input().split())

dp = [0] * 21
dp[1],dp[2],dp[3] = 1,2,4
for i in range(4, n+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

base_combi = ['', ['1'], ['1+1', '2'], ['1+1+1', '1+2', '2+1', '3']]
answer = ''
def dfs(n, k):
    global answer
    if n <= 3:
        answer += base_combi[n][k-1]
        return
    if k <= dp[n-1]:
        answer += '1+'
        dfs(n-1, k)
    elif k <= dp[n-1] + dp[n-2]:
        answer += '2+'
        dfs(n-2, k-dp[n-1])
    else:
        answer += '3+'
        dfs(n-3, k-dp[n-1]-dp[n-2])

if k > dp[n]:
    print(-1)
else:
    dfs(n ,k)

print(answer)