from copy import deepcopy
N = int(input())
A = list(map(int, input().split()))

dp_rgt, dp_lft = [1]*N, [1]*N
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp_rgt[i] = max(dp_rgt[i], dp_rgt[j]+1)
for i in range(N-2,-1,-1):
    for j in range(i+1, N):
        if A[i] > A[j]:
            dp_lft[i] = max(dp_lft[i], dp_lft[j]+1)

answer = 0
for i in range(N):
    answer = max(dp_rgt[i] + dp_lft[i] - 1, answer)
print(answer)