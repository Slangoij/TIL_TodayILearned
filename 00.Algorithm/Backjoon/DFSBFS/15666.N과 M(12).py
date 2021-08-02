import sys
input = sys.stdin.readline

N, M = map(int, input().split())
series = list(set(map(int, input().split())))
series.sort()
N = len(series)

answer = []
tmpans = []
def dfs(now, cnt):
    for i in range(now, N):
        tmpans.append(series[i])
        if cnt < M:
            dfs(i, cnt+1)
        elif len(tmpans) == M:
            answer.append(tmpans.copy())
        tmpans.pop()

dfs(0, 1)
for ans in answer:
    print(" ".join(map(str, ans)))

"""

3 1
4 5 2

4 2
9 8 7 1

"""