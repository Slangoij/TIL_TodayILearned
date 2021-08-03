import sys
input = sys.stdin.readline
from itertools import combinations

N,S = map(int,input().split())
soolst = list(map(int, input().split()))
soolst.sort()

# 2번째 풀이, 블로그 참조하였지만
# 또 시간초과가 났다.

# a = time.time()
lftlst, rgtlst = soolst[:N//2], soolst[N//2:]

# 리스트의 모든 값의 합을 구한 리스트를 각각 추가
# 여기서 시초난듯하다?
leng = len(lftlst)
sum_lft, sum_rgt = [], []
for i in range(leng+1):
    sum_lft += list(sum(com) for com in combinations(lftlst,i))
leng = len(rgtlst)
for i in range(leng+1):
    sum_rgt += list(sum(com) for com in combinations(rgtlst,i))
# sum_lft = [0]*(1<<leng)
# for i in range(1<<leng):
#     for j in range(leng):
#         if i&(1<<j):
#             sum_lft[i] += lftlst[j]

# sum_rgt = [0]*(1<<leng)
# for i in range(1<<leng):
#     for j in range(leng):
#         if i&(1<<j):
#             sum_rgt[i] += rgtlst[j]

sum_lft.sort()
sum_rgt.sort()

# print("걸린시간", int(time.time()-a),"from", a)

answer = 0
lft, rgt = 0, len(sum_rgt)-1
while lft<len(sum_lft) and rgt>=0:
    tmp_sum = sum_lft[lft]+sum_rgt[rgt]
    if tmp_sum == S:
        cnt1, cnt2 = 1, 1
        lft += 1
        rgt -= 1
        while lft<len(sum_lft) and sum_lft[lft]==sum_lft[lft-1]:
            lft += 1
            cnt1 += 1
        while rgt>=0 and sum_rgt[rgt]==sum_rgt[rgt+1]:
            rgt -= 1
            cnt2 += 1
        answer += cnt1*cnt2
    elif tmp_sum < S:
        lft += 1
    else:
        rgt -= 1

if S == 0:
    answer -= 1

print(answer)
# print("걸린시간", int(time.time()-a),"from", a)
"""

5 0
-7 -3 -2 5 8

6 3
1 1 1 -1 -1 -1

4 3
1 1 2 2

40 0
0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0  
"""
# # 1번째 시도
# # 연속된 부분집합만 가능한 줄 착각
# lft, rgt = 0, len(soolst)-1
# summ = sum(soolst)
# answer = 0
# while lft<=rgt:
#     if summ == S:
#         answer += 1
#     if summ <= S:
#         summ -= soolst[lft]
#         lft += 1
#     else:
#         summ -= soolst[rgt]
#         rgt -= 1

# print(answer)