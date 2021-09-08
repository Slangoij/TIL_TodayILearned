import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    x = input().strip()
    if x == '0':
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
        continue
    heapq.heappush(q, int(x))