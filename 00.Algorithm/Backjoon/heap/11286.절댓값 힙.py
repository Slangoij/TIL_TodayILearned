import sys
input = sys.stdin.readline
import heapq

N = int(input())
q = []
for _ in range(N):
    heappush(q, (int(input()), )