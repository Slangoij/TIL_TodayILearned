import sys
import heapq
input = sys.stdin.readline
N = int(input())
crds = []
if N == 1:
    print(0)
else:
    for _ in range(N):
        heapq.heappush(crds, int(input()))
    ans = 0
    for i in range(N-1):
        tmp = heapq.heappop(crds) + heapq.heappop(crds)
        ans += tmp
        heapq.heappush(crds, tmp)
    print(ans)



# # 첫번째 시도: 무조건 앞에서부터 계산하면 되는 줄 알았지만 중간 계산 결과가 다음 카드보다 더 크므로
# # 뒤로 넘어갈 수 있는 가능성을 간과했다.
# for _ in range(N):
#     crds.append(int(input()))
#
# crds.sort()
# cnt, answer = N-1, (N-1)*crds[0]
# for i in range(1,N):
#     answer += cnt * crds[i]
#     cnt -= 1
#
# print(answer)