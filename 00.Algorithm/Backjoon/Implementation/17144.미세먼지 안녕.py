import sys
input = sys.stdin.readline
from copy import deepcopy

R, C, T = map(int,input().split())
tmpmap = []
mapp = []
puri = []
dusts = []
for i in range(R):
    tmplst = list(map(int, input().split()))
    if tmplst[0] == -1:
        puri.append(i)
    mapp.append(tmplst)

dx = [ 0, 1, 0,-1]
dy = [ 1, 0,-1, 0]
def blow(i, j, dust):
    val = dust//5
    cnt = 0
    for dir in range(4):
        ni, nj = i+dx[dir], j+dy[dir]
        if 0<=ni<R and 0<=nj<C and not (ni in puri and nj==0):
            cnt += 1
            tmpmap[ni][nj] += val
    tmpmap[i][j] += dust - val * cnt

def purify():
    pmapp = deepcopy(tmpmap)
    pmapp[0] = tmpmap[0][1:] + [0]
    pmapp[-1] = tmpmap[-1][1:] + [0]

    for pu in puri:
        pmapp[pu] = [0] + tmpmap[pu][:-1]

    for i in range(0,puri[0]+1):
        if i<puri[0]:
            pmapp[i][-1] = tmpmap[i+1][-1]
            if 0<i:
                pmapp[i][0] = tmpmap[i-1][0]

    for i in range(puri[1],R):
        if puri[1]<i:
            pmapp[i][-1] = tmpmap[i-1][-1]
            if i<R-1:
                pmapp[i][0] = tmpmap[i+1][0]

    return pmapp
    
for _ in range(T):
    dusts.clear()
    for i in range(R):
        for j in range(C):
            if mapp[i][j] > 0:
                dusts.append([i,j,mapp[i][j]])

    tmpmap = [[0]*C for _ in range(R)]
    for ti,tj,td in dusts:
        blow(ti,tj,td)
    mapp = purify()

answer = 0
for ma in mapp:
    answer += sum(ma)

print(answer)

"""

7 8 1
0 0 0 0 0 0 0 9
0 0 0 0 3 0 0 8
-1 0 5 0 0 0 22 0
-1 8 0 0 0 0 0 0
0 0 0 0 0 10 43 0
0 0 5 0 15 0 0 0
0 0 40 0 0 0 20 0

7 8 1
1 0 0 0 0 0 0 9
1 0 0 0 3 0 0 8
-1 0 5 0 0 0 1 1
-1 8 0 0 0 0 0 0
1 0 0 0 0 10 1 1
1 0 5 0 15 0 0 1
1 0 40 0 0 0 1 1


"""