from collections import deque

T = int(input())
for _ in range(T):
    N,M = map(int, input().split())
    lst = list(map(int, input().split()))
    q = deque(lst)
    ans = 1
    while q:
        if q[0] == max(q) and M == 0:
            break
        tmp = q.popleft()
        if tmp < max(q):
            q.append(tmp)
        else:
            ans += 1
        if M == 0:
            M = len(q)
        M -= 1
    print(ans)

"""

3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1

2
4 2
1 2 3 4
6 0
1 1 9 1 1 1
"""