T = int(input())
tests = []
maxx = 0
for _ in range(T):
    N = int(input())
    tests.append(N)
    maxx = max(maxx, N)

dp = [[1,0],[0,1]]
for i in range(2,maxx+1):
    dp.append([dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]])

for test in tests:
    print(dp[test][0], dp[test][1])