import sys
import heapq
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    heapq.heappush(lst, int(input()))
while lst:
    print(heapq.heappop(lst))