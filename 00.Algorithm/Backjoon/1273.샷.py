import sys
input = sys.stdin.readline

N = int(input())
cans = []
# cans.append(list(map(int, input().split())))
# for _ in range(2):
#     tmp_lst = []
#     now_lst = list(map(int, input().split()))
#     for i in range(N):
#         tmp_lst.append(cans[-1][i] + now_lst[i])
#     cans.append(tmp_lst)
for _ in range(3):
    cans.append(list(map(int, input().split())))
M = int(input())
shots = list(map(int, input().split()))

ans = [0] * M
points = [1, 2, 5]
for i in range(M):
    now_shot = shots[i]
    for idx, can in enumerate(zip(*cans)):
        tmp_shot = now_shot
        for j in range(3):
            if tmp_shot <= can[j]:
                ans[i] += points[j]
                cans[j][idx] -= 1
                break
            tmp_shot -= can[j]
            
for an in ans:
    print(an)