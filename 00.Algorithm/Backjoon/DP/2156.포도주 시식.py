import sys
input = sys.stdin.readline

n = int(input())
wines = [0]
for _ in range(n):
    wines.append(int(input()))

if n == 1:
    print(wines[1])
elif n == 2:
    print(wines[1]+wines[2])
else:
    ans = 0
    dp = [0, [0,wines[1]], [wines[1],wines[1]+wines[2]]]
    for i in range(3, n+1):
        tmp = [0]*2
        tmp[0] = max(dp[i-1][0], dp[i-1][1])
        tmp[1] = max(dp[i-2][0]+wines[i-1], dp[i-2][1]) + wines[i]
        dp.append(tmp)
        ans = max(ans, tmp[0], tmp[1])

    print(ans)

"""

5
1
4
6
1
3

"""