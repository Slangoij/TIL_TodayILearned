import sys
input = sys.stdin.readline

strr = list(input().strip())
exp = list(input().strip())
strleng = len(strr)
expleng = len(exp)

stack = []
for i in range(strleng):
    stack.append(strr[i])
    if len(stack) >= expleng and stack[-expleng:] == exp:
        for j in range(expleng):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print('FRULA')

# # 2번째 시도: 폭발 문자열과 문자열을 인덱스하나하나 늘려가며 비교하다 복잡해서 포기
# idx, expidx = 0, 0
# stack = []
# ans = ''
# while idx < len(strr):
#     if expidx < len(exp) and strr[idx] == exp[expidx]:
#         expidx += 1
#         if expidx == len(exp):
#             expidx = 0
#     elif strr[idx] != exp[expidx] and expidx != 0:
#         stack.append(exp[:expidx])
#         expidx = 0
#         continue
#     elif stack and idx+len(exp)-len(stack[-1])<=len(strr) and exp[len(stack[-1]):] == strr[idx:idx+len(exp)-len(stack[-1])]:
#         idx += len(exp)-len(stack[-1])
#         stack.pop()
#         expidx = 0
#     else:
#         ans += "".join([stac for lst in stack for stac in lst]+strr[idx:idx+expidx+1])
#         stack.clear()
#         idx += expidx
#         expidx = 0
#     idx += 1

# 1번째 시도: 시간초과
# while strr and exp in strr:
#     strr = strr.replace(exp, '')
# if strr:
#     print(strr)
# else:
#     print('FRULA')