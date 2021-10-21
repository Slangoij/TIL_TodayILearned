import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewels, bags = [], []
for _ in range(N):
    m, v = map(int, input().split())
    heapq.heappush(jewels, (m, [m, v]))
for _ in range(K):
    heapq.heappush(bags, int(input()))

ans = 0
for i in range(K):
    crnt_bag = heapq.heappop(bags)
    able_jewels = []
    while jewels:
        crnt_jewel = heapq.heappop(jewels)[-1]
        if crnt_bag >= crnt_jewel[0]:
            heapq.heappush(able_jewels, [-crnt_jewel[-1], crnt_jewel])
        else:
            heapq.heappush(jewels, [crnt_jewel[0], crnt_jewel])
            break
    if able_jewels:
        ans += heapq.heappop(able_jewels)[-1][-1]
        while able_jewels:
            crnt_jewel = heapq.heappop(able_jewels)[-1]
            heapq.heappush(jewels, [crnt_jewel[0], crnt_jewel])
print(ans)
