import sys
from collections import deque
input = sys.stdin.readline

left = deque(list(input().strip()))
right = deque([])
cur = len(left)
for _ in range(int(input())):
    cmd = list(input().split())
    if cmd[0] == 'L':
        if len(left):
            right.appendleft(left.pop())
    elif cmd[0] == 'D':
        if len(right):
            left.append(right.popleft())
    elif cmd[0] == 'B':
        if len(left):
            left.pop()
    else:
        left.append(cmd[1])

print("".join(left+right))
