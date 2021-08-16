import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
root = [i for i in range(N+1)]
mapp = []
for _ in range(M):
    mapp.append(list(map(int, input().split())))

mapp.sort(key=lambda x: x[2])

def findroot(node):
    if node != root[node]:
        root[node] = findroot(root[node])
    return root[node]

answer = 0
for stt, end, cst in mapp:
    sroot = findroot(stt)
    eroot = findroot(end)
    if sroot != eroot:
        for i in range(1,len(root)):
            if root[i] == max(sroot, eroot):
                root[i] = min(sroot, eroot)
        # root[max(sroot, eroot)] = min(sroot, eroot)
        answer += cst

print(answer)

"""

6
9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8

"""