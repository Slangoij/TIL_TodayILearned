import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
K = int(input())
mapp = [[0]*(N+1) for _ in range(N+1)]
for _ in range(K):
    x, y = map(int, input().split())
    mapp[x][y] = 2
L = int(input())
chg_dir = []
for _ in range(L):
    tm, dir = input().split()
    chg_dir.append((int(tm), dir))

dx = [ 0,-1, 0, 1]
dy = [-1, 0, 1, 0]
now_dir = 2
now_dir_idx = 0
time = 1
cx, cy = 1,1
mapp[cx][cy] = 1
snk = deque([(1,1)])
while True:
    nx, ny = cx+dx[now_dir], cy+dy[now_dir]
    if nx<1 or nx>N or ny<1 or ny>N or mapp[nx][ny] == 1:
        break

    snk.append((nx,ny))
    if mapp[nx][ny] != 2:
        lastx, lasty = snk.popleft()
        mapp[lastx][lasty] = 0
    mapp[nx][ny] = 1
    cx, cy = nx,ny

    if now_dir_idx < len(chg_dir) and chg_dir[now_dir_idx][0] == time:
        if chg_dir[now_dir_idx][1] == 'L':
            now_dir = (now_dir-1)%4
        else:
            now_dir = (now_dir+1)%4
        now_dir_idx += 1

    time += 1

print(time)

"""

6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L

"""