import sys
import heapq
input = sys.stdin.readline

q = []
for _ in range(int(input())):
    x = int(input())
    if x:
        heapq.heappush(q, (-x, x))
    else:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)