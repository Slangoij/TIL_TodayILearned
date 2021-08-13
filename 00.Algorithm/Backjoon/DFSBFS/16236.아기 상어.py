import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
mapp = []
vstd = [[False]*N for _ in range(N)]
for i in range(N):
    tmp = list(map(int, input().split()))
    mapp.append(tmp)
    for j in range(N):
        if tmp[j] == 9:
            q = deque([[i,j,0]])
            mapp[i][j] = 0
            vstd[i][j] = True

dx = [-1, 0, 0, 1]
dy = [ 0,-1, 1, 0]
answer = 0
fish, cnt = 2, 0

while q:
    tmp_q = []
    while q:
        cx, cy, pathlen = q.popleft()
        for dir in range(4):
            nx, ny = cx+dx[dir], cy+dy[dir]
            if 0<=nx<N and 0<=ny<N and not vstd[nx][ny]:
                if mapp[nx][ny] <= fish:
                    tmp_q.append([nx,ny,pathlen+1])
                    vstd[nx][ny] = True
    tmp_q.sort(key=lambda x: (x[0], x[1]))
    for node in tmp_q:
        nx, ny, pathlen = node
        if 0 < mapp[nx][ny] < fish:
            q.clear()
            q.append([nx,ny,0])
            vstd = [[False]*N for _ in range(N)]
            vstd[nx][ny] = True
            mapp[nx][ny] = 0
            cnt += 1
            if cnt >= fish:
                fish += 1
                cnt = 0
            answer += pathlen
            break
        q.append([nx,ny,pathlen])

print(answer)

"""

3
0 0 0
0 0 0
0 9 0

3
0 0 1
0 0 0
0 9 0

3
0 0 1
0 3 3
0 9 0

3
1 3 1
3 9 3
1 3 1

4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4

5
0 0 1 0 0
0 1 0 1 0
1 0 9 0 1
0 1 0 1 0
0 0 1 0 0

5
0 0 0 0 0
0 0 0 0 0
0 0 9 0 1
0 1 0 0 0
0 0 0 0 0

6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6

6
6 0 6 0 6 1
0 0 0 0 0 2
2 3 4 5 6 6
0 0 0 0 0 2
0 2 0 0 0 0
3 9 3 0 0 1

6
1 1 1 1 1 1
2 2 6 2 2 3
2 2 5 2 2 3
2 2 2 4 6 3
0 0 0 0 0 6
0 0 0 0 0 9

6
6 0 6 0 6 1 
0 0 0 0 0 2 
2 3 4 5 6 6 
0 0 0 0 0 2 
0 2 0 0 0 0 
3 9 3 0 0 1

"""


# # 1번째 시도: 2칸 이상 떨어진 물고기들 먹는 순서가 잘못되었다.
# def chk(mapp, fish, x, y):
#     for i in range(len(mapp)):
#         for j in range(len(mapp[i])):
#             if i == x and j == y:
#                 continue
#             if 0 < mapp[i][j] < fish:
#                 return True
#     return False

# while q:
#     cx, cy, pathlen = q.popleft()
#     if not chk(mapp, fish, cx, cy):
#         break
#     for dir in range(4):
#         nx, ny = cx+dx[dir], cy+dy[dir]
#         if 0<=nx<N and 0<=ny<N and not vstd[nx][ny]:
#             if mapp[nx][ny] <= fish:
#                 q.append([nx,ny,pathlen+1])
#                 vstd[nx][ny] = True
#     if 0 < mapp[nx][ny] < fish:
#         q.clear()
#         q.append([nx,ny,0])
#         vstd = [[False]*N for _ in range(N)]
#         vstd[nx][ny] = True
#         mapp[nx][ny] = 0
#         cnt += 1
#         if cnt >= fish:
#             fish += 1
#             cnt = 0
#         answer += pathlen+1
#         break