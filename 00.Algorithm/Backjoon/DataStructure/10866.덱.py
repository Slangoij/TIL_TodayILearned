import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque([])
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push_back':
        q.append(cmd[1])
    elif cmd[0] == 'push_front':
        q.appendleft(cmd[1])
    elif cmd[0] == 'pop_front':
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if len(q):
            print(q.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        print(int(len(q)<1))
    elif cmd[0] == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)