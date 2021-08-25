import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
dp = [x for x in A]
for i in range(1, n):
    for j in range(i):
        if A[i]>A[j]:
            dp[i]=max(dp[i],dp[j]+A[i])
print(max(dp))


"""

10
1 100 2 50 60 3 5 6 7 8

3
3 2 1

3
1 2 1

9
10 2 9 1 2 3 4 7 6

5
5 1 2 3 10

5
3 2 1 2 3


"""


# # 1번째 시도: 그당시 하나하나의 최소값, 최대값과 수열합을 dp에 추가해가려했으나
# # 점점 조회할 값이 많아지므로 포기
# dp = [[A[0],A[0],A[0]]] # 수열 첫번째, 마지막, 수열 합
# for i in range(1,len(A)):
#     for j in range(len(dp)):
#         if A[i] < dp[j][0]:
#             dp.append([A[i],A[i],A[i]])
#         elif A[i] > dp[j][0]+ if A[i] < dp[j][1]:
#                 dp.append([dp[j][0],A[i],dp[j][2]+A[i]])
#             else:
#                 dp.append([dp[j][0],A[i],dp[j][2]+A[i]])
# dp.sort(key=lambda x: -x[2])
# print(dp[0][2])


# # 2번째 시도: 이유를 몰겠네
# dp = [num for num in range(1001)]
# to_srch = [A[0]]
# dp[A[0]] = A[0]
# srch_lst = []
# for i in range(1,n):
#     nownum = A[i]
#     to_srch.append(nownum)
#     srch_lst = [dp[j] for j in to_srch if j<nownum]
#     nowmax = 0
#     if srch_lst:
#         nowmax = max(srch_lst)
#     dp[nownum] += nowmax

# print(max([dp[j] for j in to_srch]))