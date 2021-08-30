import sys
N = int(input())
bilds = list(map(int, input().split()))

ans = 0
for i in range(N):
    tmpans = 0
    lft = []
    for j in range(i):
        lft.append((bilds[i]-bilds[j])/(i-j))
    for j in range(len(lft)):
        if lft[j] == min(lft[j:]) and lft[j:].count(lft[j]) == 1:
            tmpans += 1
        # # 여기서 같은 기울기를 가지는 여러 건물을 찾아내지 못하는 것 발견!
        # if lft[j] == min(lft[j:]):
        #     tmpans += 1
    rgt = []
    for j in range(i+1,N):
        rgt.append((bilds[i]-bilds[j])/(i-j))
    for j in range(len(rgt)):
        if rgt[j] == max(rgt[:j+1]) and rgt[:j+1].count(rgt[j]) == 1:
            tmpans += 1
    ans = max(ans, tmpans)

print(ans)

"""

15
1 5 3 2 6 3 2 6 4 2 5 7 3 1 5

5
1 5 3 2 4

7
3 1 3 4 3 1 3

"""

# # 다른 사람 풀이

# n = int(input())
# data = list(map(int, input().split()))
# zeros = [0] * n # 해당 층에서 보이는 빌딩 개수 저장

# # 2중 for문으로 모든 빌딩 비교
# for i in range(n):
#   check = -1e9
#   for j in range(i + 1, n):
#     # 기울기 계산
#     slope = (data[j] - data[i]) / (j - i)
#     # 빌딩에 가리지 않는 경우
#     if slope > check:
#       # 최종적으로 i번째에서 기울기가 제일 큰 값 저장
#       check = slope
#       # 서로 볼 수 있기 때문에 +1
#       zeros[i] += 1
#       zeros[j] += 1
      
# result = 0
# # 가장 많은 고층 빌딩이 보이는 빌딩
# for i in zeros:
#   result = max(result, i)
# print(result)