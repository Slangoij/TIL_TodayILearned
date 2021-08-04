import sys
input = sys.stdin.readline

N = int(input())
aplcnts = list(map(int, input().split()))
B, C = map(int, input().split())

answer = N
for aplcnt in aplcnts:
    if aplcnt>B:
        answer += (aplcnt-B+C-1)//C

print(answer)

"""

5
1000000 1000000 1000000 1000000 1000000
5 7

3
3 4 5
2 2

5
1 2 3 4 5
2 2

"""