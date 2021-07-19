"""
4
10 8
-7 9 2 -4 12 1 5 -3 -2 0
10 4
-7 9 2 -4 12 1 5 -3 -2 0
4 20
1 7 3 5
5 10
3 9 7 1 5
"""


import sys
import os

t = int(input())
answer = []
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    soo_list = list(map(int, sys.stdin.readline().split()))
    soo_list.sort()

    lft, rgt = 0, n-1
    crnt_gap, crnt_cnt = 999999999, 1
    while lft < rgt:
        tmp_sum = soo_list[lft] + soo_list[rgt]
        if tmp_sum < k:
            lft += 1
        else:
            rgt -= 1
        
        tmp_gap = abs(tmp_sum - k)
        if tmp_gap < crnt_gap:
            crnt_gap = tmp_gap
            crnt_cnt = 1
        elif tmp_gap == crnt_gap:
            crnt_cnt += 1
    answer.append(crnt_cnt)

for ans in answer:
    print(ans)