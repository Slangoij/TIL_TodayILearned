from collections import deque

n, k = map(int, input().split())

q = deque([n])
vstd = [0]*200001
while q:
    now_node = q.popleft()
    if now_node == k:
        print(vstd[now_node])
        break
    for crnt_node in [now_node-1, now_node+1, now_node*2]:
        if 0 <= crnt_node <= 200000 and not vstd[crnt_node]:
            vstd[crnt_node] = vstd[now_node] + 1
            q.append(crnt_node)

"""
99999 100000
100000 99999
"""