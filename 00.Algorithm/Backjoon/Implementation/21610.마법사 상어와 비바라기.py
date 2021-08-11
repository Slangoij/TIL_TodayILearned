import sys
input = sys.stdin.readline

N,M = map(int, input().split())
mapp = [[0]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    mapp[i][1:] = list(map(int, input().split()))
moves = []
for _ in range(M):
    moves.append(list(map(int, input().split())))


gurums = [[N-1,1],[N-1,2],[N,1],[N,2]]
dir = [[],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1]]
for mvdir, mvlen in moves:
    to_magic = []
    vstd = [[False]*(N+1) for _ in range(N+1)]
    for gx,gy in gurums:
        nx = (gx + (dir[mvdir][0] * mvlen)-1)%N + 1
        ny = (gy + (dir[mvdir][1] * mvlen)-1)%N + 1
        mapp[nx][ny] += 1
        to_magic.append([nx,ny])
        vstd[nx][ny] = True

    for tx,ty in to_magic:
        cnt = 0
        for dx,dy in [[-1,-1],[1,-1],[-1,1],[1,1]]:
            tmpx, tmpy = tx+dx, ty+dy
            if 0<tmpx<=N and 0<tmpy<=N and mapp[tmpx][tmpy]:
                cnt += 1
        mapp[tx][ty] += cnt
    gurums.clear()

    for i in range(1,N+1):
        for j in range(1,N+1):
            if not vstd[i][j] and mapp[i][j]>=2:
                gurums.append([i,j])
                mapp[i][j] -= 2

summ = 0
for ma in mapp:
    summ += sum(ma)

print(summ)


"""

5 4
0 0 1 0 2
2 3 2 1 0
4 3 2 9 0
1 0 2 9 0
8 8 2 1 0
1 3
3 4
8 1
4 8

5 8
0 0 1 0 2
2 3 2 1 0
0 0 2 0 0
1 0 2 0 0
0 0 2 1 0
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2

5 8
100 100 100 100 100
100 100 100 100 100
100 100 100 100 100
100 100 100 100 100
100 100 100 100 100
8 1
7 1
6 1
5 1
4 1
3 1
2 1
1 1


"""