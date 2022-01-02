import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

dx = [ 0,-1, 0, 1]
dy = [-1, 0, 1, 0]
def bfs(nx, ny, hgt, now_vstd):
    q = deque([(nx, ny)])
    while q:
        cx, cy = q.popleft()
        for dir in range(4):
            nx, ny = cx+dx[dir], cy+dy[dir]
            if nx in range(n) and ny in range(n) and not now_vstd[nx][ny]\
                    and mapp[nx][ny] not in range(hgt+1):
                q.append((nx, ny))
                now_vstd[nx][ny] = True

if __name__=="__main__":
    n = int(input())
    mapp = []
    ans = 0
    for _ in range(n):
        mapp.append(list(map(int, input().split())))
    for hgt in range(0, 101):
        tmpans = 0
        vstd = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if not vstd[i][j] and mapp[i][j] not in range(hgt+1):
                    tmpans += 1
                    vstd[i][j] = True
                    bfs(i, j, hgt, vstd)
        ans = max(ans, tmpans)
    print(ans)

"""
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7
"""