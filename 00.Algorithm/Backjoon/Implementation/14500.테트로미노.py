import sys
from copy import deepcopy
input = sys.stdin.readline

def rot(ary):
    tmpary = []
    minx, miny = 1001, 1001
    for i in ary:
        minx = min(minx, i[1])
        miny = min(miny, -i[0])
    for i in ary:
        tmpary.append([i[1]-minx,-i[0]-miny])
    
    return sorted(tmpary)

def opp(ary):
    tmpary = []
    minx, miny = 1001, 1001
    for i in ary:
        minx = min(minx, -i[0])
        miny = min(miny, i[1])
    for i in ary:
        tmpary.append([-i[0]-minx, i[1]-miny])
    
    return sorted(tmpary)

def allcoord():
    allshp = []
    allshp.append(sorted([[0,0],[0,1],[0,2],[0,3]]))
    allshp.append(sorted([[0,0],[0,1],[1,0],[1,1]]))
    allshp.append(sorted([[0,0],[1,0],[2,0],[2,1]]))
    allshp.append(sorted([[0,0],[1,0],[1,1],[2,1]]))
    allshp.append(sorted([[0,0],[0,1],[0,2],[1,1]]))
    
    tmpshps = deepcopy(allshp)
    for i in allshp:
        for _ in range(4):
            chk = False
            tmparr = rot(i)
            if tmparr not in tmpshps:
                tmpshps.append(tmparr)
                chk = True
            tmpopp = opp(tmparr)
            if tmpopp not in tmpshps:
                tmpshps.append(tmpopp)
                chk = True
            i = tmparr
            if not chk:
                break

    return tmpshps

maxx = 0
N,M = map(int, input().split())
mapp = []
for _ in range(N):
    mapp.append(list(map(int, input().split())))

allcord = allcoord()
for nowshp in allcord:
    nowxmax = max(list(zip(*nowshp))[0])
    nowymax = max(list(zip(*nowshp))[1])
    for i in range(N):
        if i + nowxmax >= N:
            break
        for j in range(M):
            if j + nowymax >= M:
                break
            tmpmaxx = 0
            for dx,dy in nowshp:
                tmpmaxx += mapp[i+dx][j+dy]
            # maxx = max(maxx, tmpmaxx)
            if tmpmaxx > maxx:
                maxx = tmpmaxx

print(maxx)

"""


5 5
1 2 3 4 5
5 4 3 2 1
2 3 4 5 6
6 5 4 3 2
1 2 1 2 1

4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

4 10
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1
1 2 1 2 1 2 1 2 1 2
2 1 2 1 2 1 2 1 2 1

3 3
1 1 1
2 1 1
2 2 2



"""