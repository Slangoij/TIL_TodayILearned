import sys
input = sys.stdin.readline

n = int(input())
todolst = list(map(int, input().split()))
stack, ans = [[0, todolst[0]]], [0]
for i in range(1, n):
    if stack[-1][1] < todolst[i]:
        while stack and stack[-1][1] < todolst[i]:
            stack.pop()
    if stack:
        ans.append(stack[-1][0]+1)
    else:
        ans.append(0)
    stack.append([i, todolst[i]])
print(" ".join(map(str, ans)))

# # 1번째 시도: 큐로 최대값보다 클 때만 클리어하고 항상 남아있는 큐에서 현재값
# import heapq
# q = []
# n = int(input())
# anslst = []
# todolst = list(map(int, input().split()))
# for i in range(n):
#     if q:
#         for j in range(len(q)):
#             if -q[j][0] > todolst[i]:
#                 anslst.append(str(q[j][1]+1))
#                 break
#         if todolst[i] > -q[0][0]:
#             q.clear()
#     else:
#         anslst.append('0')
#     heapq.heappush(q, (-todolst[i], i))
# print(" ".join(anslst))
