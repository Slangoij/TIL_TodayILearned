import sys
input = sys.stdin.readline

S = input().strip()
N = int(input())
words = []
for _ in range(N):
    words.append(input().strip())
# 4번째 풀이
# 다른 사람 풀이 참고
dp = [0]*101
dp[0] = 1

leng = len(S)
for i in range(leng):
    if dp[i]:
        for word in words:
            wordleng = len(word)
            if S[i:i+wordleng] == word:
                dp[i+wordleng] = 1

print(dp[leng])


"""

softwarecontest
2
software
contest

aaaaaaaaaa
2
aaaa
aaa

"""


# # 1번째 풀이
# # 무조건 단어가 다 다르다고 착각하여 고민없이 나온 해답
# for word in words:
#     S = S.replace(word, ' ')

# if S.split():
#     print('0')
# else:
#     print('1')

# # 2번째 풀이
# # 백트래킹으로 해결, 시간초과
# answer = 0
# def dfs(nowword, leng):
#     global answer
#     if nowword == S:
#         answer = 1
#         return
#     for word in words:
#         if len(nowword+word) <= leng:
#             dfs(nowword+word, leng)
# dfs('', len(S))
# print(answer)


# # 3번째 풀이
# # 다른 사람의 설명을 참고해 dp로 풀라는 것만 보고 내 자신의 방법으로
# # dp를 새롭게 메모이제이션해가면서 만들수있는 모든 경우를 따졌다.
# # 하지만 다른 풀이를 보면서 느낀대로 역시 기존의 데이터를 갖고 변형하는 식으로
# # 푸는 것이 맞다는 것을 확인
# leng = len(S)
# def dp():
#     dp = [['']]
#     for i in range(101):
#         tmplst = []
#         for nowword in dp[i]:
#             minleng = 1e9
#             for word in words:
#                 addfrnt, addback = word+nowword, nowword+word
#                 minleng = min(minleng, len(addfrnt), len(addback))
#                 if addfrnt==S or addback==S:
#                     return 1
#                 tmplst.append(addfrnt)
#                 tmplst.append(addback)
#             if minleng > leng:
#                 return 0
#         dp.append(list(set(tmplst)))

# print(dp())