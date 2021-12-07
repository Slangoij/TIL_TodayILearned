import sys
import heapq
input = sys.stdin.readline
inf = int(1e9)

v, e = map(int, input().split())
k = int(input())
mapp = {i: {} for i in range(1, v+1)}
for _ in range(e):
    uu, vv, ww = map(int, input().split())
    if mapp.get(uu, 0) != 0 and mapp.get(uu, 0).get(vv, 0) != 0:
        mapp[uu][vv] = min(mapp[uu][vv], ww)
    else:
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

"""
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
"""