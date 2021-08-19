import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
from copy import deepcopy

# 3번째 시도: 0의 개수를 각 조합의 각 반복에서 전체 맵을 확인하는게 아닌
# 0 전체 개수 확인해서 전파할때마다 감소시키는 트릭
N, M = map(int,input().split())
mapp = []
virs = []
dx = [ 0,-1, 0, 1]
dy = [-1, 0, 1, 0]
answer = int(1e9)
cnt0 = 0
for i in range(N):
    tmplst = list(map(int, input().split()))
    for j in range(N):
        if tmplst[j] == 2:
            virs.append([i,j])
            tmplst[j] = -3 # 먼저 전체를 비활성화하고 필요한 활성바이러스만 나중에 따로 치환
        elif tmplst[j] == 1:
            tmplst[j] = -1 # 벽은 -1로 치환
        elif tmplst[j] == 0:
            cnt0 += 1     # 0 전체 개수 미리 저장
    mapp.append(tmplst)

def spread(actvirs):
    tmpmap = deepcopy(mapp)
    lftcnt, maxtime = cnt0, 0
    q = deque([])
    for x,y in actvirs:
        tmpmap[x][y] = -2 # 활성 바이러스: -2
        q.append([x,y,0])
    while lftcnt and q:
        ci, cj, ct = q.popleft()
        for dir in range(4):
            ni, nj, nt = ci+dx[dir], cj+dy[dir], ct+1
            if 0<=ni<N and 0<=nj<N and tmpmap[ni][nj] in [0, -3]:
                if tmpmap[ni][nj] == 0:
                    lftcnt -= 1
                tmpmap[ni][nj] = nt
                q.append([ni,nj,nt])
                maxtime = max(maxtime, nt)
                
    if lftcnt:
        return -1
    return maxtime

chkavail = -1
for vir in list(combinations(virs, M)):
    tmpan = spread(vir)
    chkavail = max(chkavail, tmpan)
    if tmpan != -1:
        answer = min(answer, tmpan)

if chkavail != -1:
    print(answer)
else:
    print(-1)



"""

7 3
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2

4 2
0 1 1 0
2 1 1 2
2 1 1 2
0 1 1 0

5 1
2 2 2 1 1
2 1 1 1 1
2 1 1 1 1
2 1 1 1 1
2 2 2 2 0

7 2
2 0 1 0 0 0 0
0 0 1 0 0 2 0
0 0 1 0 0 0 0
2 0 1 0 0 0 2
0 0 1 0 0 0 0
1 1 1 1 1 1 1
2 0 1 0 2 0 0

"""

# # 1번째 시도: 문자로 치환해서 연산에 비효율, vir를 활성과 비활성으로 구분시
# # 모든 조합의 경우의 수가 큰데 이를 변형하는 데서도 비효율
# for i in range(N):
#     tmplst = list(map(int, input().split()))
#     for j in range(N):
#         if tmplst[j] == 2:
#             virs.append([i,j])
#         elif tmplst[j] == 1:
#             tmplst[j] = '-'
#     mapp.append(tmplst)

# def chk(maps):
#     for i in range(len(maps)):
#         for j in range(len(maps[i])):
#             if maps[i][j] == 0:
#                 return False
#     return True

# def spread(vir):
#     tmpmap = deepcopy(mapp)
#     q = deque([])
#     for tmpvir in virs:
#         if tmpvir not in vir:
#             tmpmap[tmpvir[0]][tmpvir[1]] = '*'
#     for vi in vir:
#         q.append(vi+[0])
#         tmpmap[vi[0]][vi[1]] = 'v'
#     while q:
#         if chk(tmpmap):
#             break
#         ci, cj, ct = q.popleft()
#         for dir in range(4):
#             ni, nj, nt = ci+dx[dir], cj+dy[dir], ct+1
#             if 0<=ni<N and 0<=nj<N and tmpmap[ni][nj] == 0:
#                 q.append([ni,nj,nt])
#                 tmpmap[ni][nj] = nt
#     tmpans = 0
#     for tmps in tmpmap:
#         for tmp in tmps:
#             if tmp not in ['*','v','-']:
#                 tmpans = max(tmpans, tmp)
#             if tmp == 0:
#                 return -1

#     return tmpans

# chkavail = -1
# for vir in list(combinations(virs, M)):
#     tmpan = spread(vir)
#     chkavail = max(chkavail, tmpan)
#     if tmpan != -1:
#         answer = min(answer, tmpan)

# if chkavail != -1:
#     print(answer)
# else:
#     print(-1)



# # 2번째 시도: 아무래도 전체 맵을 중간중간 다 퍼졌는지 확인하는 chk함수도 시간 잡아먹는듯
# N, M = map(int,input().split())
# mapp = []
# virs = []
# dx = [ 0,-1, 0, 1]
# dy = [-1, 0, 1, 0]
# answer = int(1e9)
# cnt0 = 0
# for i in range(N):
#     tmplst = list(map(int, input().split()))
#     for j in range(N):
#         if tmplst[j] == 2:
#             virs.append([i,j])
#             tmplst[j] = -3 # 먼저 전체를 비활성화하고 필요한 활성바이러스만 나중에 따로 치환
#         elif tmplst[j] == 1:
#             tmplst[j] = -1 # 벽은 -1로 치환
#         elif tmplst[j] == 0:
#             cnt0 += 1
#     mapp.append(tmplst)

# def spread(actvirs):
#     tmpmap = deepcopy(mapp)
#     lftcnt = cnt0
#     q = deque([])
#     for x,y in actvirs:
#         tmpmap[x][y] = -2 # 활성 바이러스: -2
#         q.append([x,y,0])
#     while lftcnt and q:
#         tmpchk = False
#         for line in tmpmap:
#             if 0 in line:
#                 tmpchk = True
#         if not tmpchk:
#             break
#         ci, cj, ct = q.popleft()
#         for dir in range(4):
#             ni, nj, nt = ci+dx[dir], cj+dy[dir], ct+1
#             if 0<=ni<N and 0<=nj<N and tmpmap[ni][nj] in [0, -3]:
#                 tmpmap[ni][nj] = nt
#                 q.append([ni,nj,nt])
#                 lftcnt -= 1
#     tmpans = 0
#     for tmps in tmpmap:
#         tmpans = max(tmpans, max(tmps))
#         if 0 in tmps:
#             return -1

#     return tmpans