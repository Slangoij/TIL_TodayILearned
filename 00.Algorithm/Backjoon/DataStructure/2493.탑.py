import sys
import heapq
input = sys.stdin.readline

q = []
n = int(input())
anslst = []
todolst = list(map(int, input().split()))
for i in range(n):
    if q and todolst[i] <= -q[0][0]:
        anslst.append(str(q[0][1]+1))
        q.clear()
    else:
        anslst.append('0')
    heapq.heappush(q, (-todolst[i], i))
print(" ".join(anslst))
