N, K = map(int, input().split())
q = [i for i in range(1,N+1)]
answer = []
# 두번째 시도: 굳이 다 계속 뒤에 넣을 필요없이
# 해당 부분만 팝해서 뒤에 넣으면 된다.
# 정답도 for문 필요없이 문자열이므로 join 활용 가능
idx = 0
while q:
    idx = (idx + K - 1) % len(q)
    answer.append(q.pop(idx))
print("<", ", ".join(map(str, answer)), ">", sep="")

# # 첫번째 시도: 맞았으나 답안에 더욱 좋은 풀이 확인하였다.
# from collections import deque
# q = deque([i for i in range(1,N+1)])
# answer = []
# while q:
#     for i in range(K-1):
#         q.append(q.popleft())
#     answer.append(q.popleft())
# print('<', end='')
# for i in range(len(answer)-1):
#     print(answer[i], end=', ')
# print(f'{answer[-1]}>')