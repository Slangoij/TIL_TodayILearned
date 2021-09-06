import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = deque([])

for _ in range(N):
    ordr = input().split()
    if ordr[0] == 'push':
        q.append(ordr[1])
    elif ordr[0] == 'pop':
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif ordr[0] == 'size':
        print(len(q))
    elif ordr[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif ordr[0] == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
    else: # back
        if len(q):
            print(q[-1])
        else:
            print(-1)