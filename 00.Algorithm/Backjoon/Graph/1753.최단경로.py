import sys
import heapq
input = sys.stdin.readline
inf = int(1e9)

v, e = map(int, input().split())
k = int(input())
mapp = {i: {} for i in range(1, v+1)}
for _ in range(e):
    uu, vv, ww = map(int, input().split())
    mapp[uu][vv] = ww


def dijkstra(maps, stt):
    dists = {i: inf for i in maps}
    dists[stt] = 0
    q = []
    heapq.heappush(q, [dists[stt], stt])

    while q:
        crnt_dist, crnt_node = heapq.heappop(q)
        if crnt_dist > dists[crnt_node]:
            continue
        for new_node, new_dist in maps[crnt_node].items():
            dist = crnt_dist + new_dist
            if dist < dists[new_node]:
                dists[new_node] = dist
                heapq.heappush(q, [dist, new_node])

    return dists


for ans in dijkstra(mapp, k).values():
    if ans == inf:
        print('INF')
    else:
        print(ans)
