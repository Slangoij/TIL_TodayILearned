import sys
input = sys.stdin.readline

S = input().strip()
tags, words = [], []
stt = 0
istag = False
for idx in range(len(S)):
    lett = S[idx]
    if lett == '<':
        tmp = []
        for word in list(S[stt:idx].split()):
            tmp.append("".join(list(reversed(word))))
        words.append(" ".join(tmp))
        stt = idx
        istag = True
    elif lett == '>':
        tags.append(S[stt:idx+1])
        stt = idx + 1
        istag = False
    elif not istag:
        stt = idx
        istag = True
if istag:
    words.append(S[stt:])

ans = "".join(list(map("".join, list(zip(words[:len(tags)], tags)))))
if istag:
    tmp = []
    for word in list(words[-1].split()):
        tmp.append("".join(list(reversed(word))))
    ans += " ".join(tmp)
print(ans)

"""

baekjoon online judge
<a>bd<c>
<open>tag<close>
tag<open>csr<close>
<int><max>2147483647<long long><max>9223372036854775807
<i><m>2<l l><m>9

"""


# # 1번째 시도: 태그와 단어 따로 저장에 마지막에 순서고려하여 합치려 하였다.
# S = input().strip()
# words, tags = [], []
# istag, isword = False, False
# stt, end = 0,0
# tmp = ""
# for idx in range(len(S)):
#     if S[idx] == '<':
#         if stt != idx and isword:
#             words.append(S[stt:idx])
#         stt = idx
#         istag, isword = True, False
#     elif S[idx] == '>':
#         tags.append(S[stt:idx+1])
#         stt = idx
#         istag, isword = False, True
#     elif not istag and not isword and stt!=idx:
#         if tmp:
#             tags.append(tmp)
#         stt = idx
#         isword = True
# if isword:
#     words.append(S[end+1:])
#
# ans = ''
# wordslen = len(words)
# tagslen = len(tags)
# if wordslen > tagslen:
#     if S[0] == '<':
#         for i in range(tagslen):
#             ans += tags[i]
#             tmp = []
#             for word in words[i].split():
#                 tmp.append("".join(reversed(word)))
#             ans += " ".join(tmp)
#     else:
#         for i in range(tagslen):
#             tmp = []
#             for word in words[i].split():
#                 tmp.append("".join(reversed(word)))
#             ans += " ".join(tmp)
#             ans += tags[i]
#     for i in range(tagslen, wordslen):
#         tmp = []
#         for word in words[i].split():
#             tmp.append("".join(reversed(word)))
#         ans += " ".join(tmp)
# else:
#     if S[0] == '<':
#         for i in range(wordslen):
#             ans += tags[i]
#             tmp = []
#             for word in words[i].split():
#                 tmp.append("".join(reversed(word)))
#             ans += " ".join(tmp)
#     else:
#         for i in range(wordslen):
#             tmp = []
#             for word in words[i].split():
#                 tmp.append("".join(reversed(word)))
#             ans += " ".join(tmp)
#             ans += tags[i]
#     for i in range(wordslen, tagslen):
#         ans += tags[i]
#
# print(ans)