import sys
input = sys.stdin.readline

strr = input().strip()
exp = input().strip()
while strr and exp in strr:
    strr = strr.replace(exp, '')
if strr:
    print(strr)
else:
    print('FRULA')