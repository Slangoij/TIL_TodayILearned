import sys
import re
input = sys.stdin.readline

N = int(input())
to_sol = []
for _ in range(N):
    to_sol.append(input())

p = re.compile('(100+1+|01)+')
for sol in to_sol:
    if p.search(sol):
        if p.fullmatch(sol[:-1]):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')

"""

1
10011001

3
10010111
011000100110001
0110001011001

"""
# 1번째 시도: 풀기전부터 ㅈ어규식이란 힌트 확인 
# stt, end = p.fullmatch(sol).span()
# if stt == 0 and end == len(sol)-1: