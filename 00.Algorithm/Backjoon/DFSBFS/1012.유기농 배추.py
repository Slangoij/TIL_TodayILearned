import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 1, 0,-1]
dy = [1, 0,-1, 0]
vstd = []
que = deque([])
def bfs(x, y, N, M):
    que.append([x,y])
    vstd[x][y] = True
    while que:
        cx, cy = que.popleft()
        for dir in range(4):
            nx, ny = cx + dx[dir], cy + dy[dir]
            if 0<=nx<N and 0<=ny<M and not vstd[nx][ny]:
                que.append([nx, ny])
                vstd[nx][ny] = True


T = int(input())
answer = []
for _ in range(T):
    M, N, K = map(int, input().split())
    vstd = [[True]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        vstd[y][x] = False
    
    ans = 0
    for i in range(N):
        for j in range(M):
            if not vstd[i][j]:
                bfs(i, j, N, M)
                ans += 1

    answer.append(ans)

for an in answer:
    print(an)

"""

2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0

"""