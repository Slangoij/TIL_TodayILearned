import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int, input().split())
riped = []
vstd = [[False]*M for _ in range(N)]
for i in range(N):
    tmp = list(input().strip().split())
    for j in range(M):
        if tmp[j] == '1':
            riped.append((i,j,0))
            vstd[i][j] = True
        elif tmp[j] == '-1':
            vstd[i][j] = True

def main():
    q = deque(riped)
    dx, dy = [0,-1,0,1], [1,0,-1,0]
    answer = 0
    while q:
        x,y,days = q.popleft()
        for dir in range(4):
            nx, ny = x+dx[dir], y+dy[dir]
            if 0<=nx<N and 0<=ny<M and not vstd[nx][ny]:
                q.append((nx,ny,days+1))
                vstd[nx][ny] = True
                answer = max(answer, days+1)

    for vstd_line in vstd:
        if False in vstd_line:
            return -1
            
    return answer
    
print(main())