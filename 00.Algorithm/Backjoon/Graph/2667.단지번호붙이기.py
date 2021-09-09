import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    global mapp, anslst
    q = deque([(i,j)])
    mapp[i][j] = 0
    tmpans = 1
    while q:
        x,y = q.popleft()
        for dir in range(4):
            nx,ny = x+dx[dir],y+dy[dir]
            if 0<=nx<N and 0<=ny<N and mapp[nx][ny]:
                q.append((nx,ny))
                mapp[nx][ny] = 0
                tmpans += 1
    anslst.append(tmpans)

N = int(input())
mapp = []
dx, dy = [0,1,0,-1],[1,0,-1,0]
answer = 0
anslst = []
for _ in range(N):
    mapp.append(list(map(int, list(input().strip()))))

for i in range(N):
    for j in range(N):
        if mapp[i][j]:
            bfs(i,j)
            answer += 1

print(answer)
print("\n".join(list(map(str,sorted(anslst)))))