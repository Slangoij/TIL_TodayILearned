import sys
input = sys.stdin.readline

strr = input().strip()
exp = input().strip()

idx, expidx = 0, 0
stack = []
ans = ''
while idx < len(strr):
    if expidx < len(exp) and strr[idx] == exp[expidx]:
        expidx += 1
    elif expidx == len(exp):
        expidx = 0
    elif strr[idx] != exp[expidx] and expidx != 0:
        stack.append(exp[:expidx])
    elif stack and stack[-1] == strr[idx:idx+len(stack[-1])+1]:
        stack.pop()
        idx += expidx + 1
        expidx = 0
    else:
        ans += strr[idx:idx+expidx+1]
        idx += expidx
        expidx = 0
    idx += 1

if ans:
    print(ans)
else:
    print('FRULA')

# while strr and exp in strr:
#     strr = strr.replace(exp, '')
# if strr:
#     print(strr)
# else:
#     print('FRULA')