import sys
import heapq
from collections import deque
input = sys.stdin.readline

T = int(input())
answer = []

for _ in range(T):
    n,k = map(int, input().split())
    bldtm = list(map(int, input().split()))

    graph = {key:{} for key in range(n+1)}
    distance = [0] * (n+1)
    for _ in range(k):
        x,y = map(int, input().split())
        graph[x][y] = bldtm[x-1]
    w = int(input())

    que = []
    heapq.heappush(que, (0, 1))
    distance[1] = 0
    while que:
        dist, now = heapq.heappop(que)
        if distance[now] > dist:
            continue
        for i in graph[now]:
            cost = dist + graph[now][i]
            if cost > distance[i]:
                distance[i] = cost
                heapq.heappush(que, (cost, i))

    answer.append(distance[w] + bldtm[w-1])

for ans in answer:
    print(ans)

"""


2
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
8 8
10 20 1 5 8 7 1 43
1 2
1 3
2 4
2 5
3 6
5 7
6 7
7 8
7



5
3 2
1 2 3
3 2
2 1
1
4 3
5 5 5 5
1 2
1 3
2 3
4
5 10
100000 99999 99997 99994 99990
4 5
3 5
3 4
2 5
2 4
2 3
1 5
1 4
1 3
1 2
4
4 3
1 1 1 1
1 2
3 2
1 4
4
7 8
0 0 0 0 0 0 0
1 2
1 3
2 4
3 4
4 5
4 6
5 7
6 7
7


1
3 2
1 2 3
3 2
2 1
1
"""