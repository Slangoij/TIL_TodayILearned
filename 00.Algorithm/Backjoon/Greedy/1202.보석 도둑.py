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
able_jewels = []
for i in range(K):
    crnt_bag = heapq.heappop(bags)
    while jewels and jewels[0][0] <= crnt_bag:
        crnt_m, crnt_v = heapq.heappop(jewels)[-1]
        heapq.heappush(able_jewels, (-crnt_v, [crnt_m, crnt_v]))
    if able_jewels:
        ans += heapq.heappop(able_jewels)[-1][-1]
    elif not jewels:
        break
print(ans)
