import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    mapp = []
    for _ in range(2):
        mapp.append(list(map(int, input().split())))
    dp = [[mapp[0][0], mapp[1][0]], [mapp[1][0]+mapp[0][1], mapp[0][0]+mapp[1][1]]]
    for i in range(2,n):
        dp.append([max(dp[i-2][1], dp[i-1][1])+mapp[0][i],
                   max(dp[i-2][0], dp[i-1][0])+mapp[1][i]])
    print(max(dp[-1]))
