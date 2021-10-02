import sys
import copy
input = sys.stdin.readline

def chk(strs):
    cnt = 0
    newlst = strs.split('X')
    for space in newlst:
        if len(space) >= 2:
            cnt += 1
    return cnt

n = int(input())
tmp = [list(input().strip()) for _ in range(n)]
mapforhor = copy.deepcopy(tmp)
mapforver = list(zip(*(copy.deepcopy(tmp))))
hor, ver = 0,0
for i in range(n):
    hor += chk("".join(mapforhor[i]))
for i in range(n):
    ver += chk("".join(mapforver[i]))

print(hor, ver)
