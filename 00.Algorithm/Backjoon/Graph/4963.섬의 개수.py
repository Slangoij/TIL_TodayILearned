import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,-1,-1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0,-1,-1]
vstd = []


def bfs(x, y, mapp):
    global vstd
    vstd[x][y] = True
    q = deque([(x, y)])
    while q:
        crnt_x, crnt_y = q.popleft()
        for dir in range(8):
            next_x, next_y = crnt_x + dx[dir], crnt_y + dy[dir]
            if next_x in range(h) and next_y in range(w)\
                    and not vstd[next_x][next_y] and mapp[next_x][next_y] == 1:
                vstd[next_x][next_y] = True
                q.append((next_x, next_y))


def solution(w, h):
    global vstd
    ans = 0
    mapp = []
    vstd = [[False] * w for _ in range(h)]

    for _ in range(h):
        mapp.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if not vstd[i][j] and mapp[i][j] == 1:
                ans += 1
                bfs(i, j, mapp)

    return ans

if __name__ == "__main__":
    w, h = map(int, input().split())
    while w != 0 and h != 0:
        print(solution(w, h))
        w, h = map(int, input().split())

"""
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
"""