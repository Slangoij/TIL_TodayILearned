N = int(input())
steps = [0]
for _ in range(N):
    steps.append(int(input()))

if N == 1:
    print(steps[1])
elif N == 2:
    print(steps[1]+steps[2])
else:
    dp = [0, [0,steps[1]], [steps[1],steps[1]+steps[2]]]
    for i in range(3, N+1):
        tmp = [0]*2
        tmp[0] = dp[i-1][1]
        tmp[1] = max(dp[i-2][0]+steps[i-1], dp[i-2][1]) + steps[i]
        dp.append(tmp)
    print(dp[N][1])

"""

6
10
20
15
25
10
20

6
2
4
3
5
2
4

3
2
3
1

"""










# # 첫번째 시도: 무조건 3번마다 쉬고 00x 0x00 x00 이런식으로 패턴을
# # 반복하는게 당시의 최대값인 줄로 이해했다.
# dp = [0, [0,steps[1]], [steps[1]+steps[2],steps[1],steps[2]]]
# for i in range(3, N+1):
#     tmp = []
#     for j in range(3):
#         if (-i)%3 == j:
#             tmp.append(dp[i-1][j])
#         else:
#             tmp.append(dp[i-1][j]+steps[i])
#     dp.append(tmp)

# ans = 0
# for i in range(3):
#     if (-N)%3 != i:
#         ans = max(ans,dp[N][i])
# print(ans)