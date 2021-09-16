import sys
input = sys.stdin.readline

def sol(strr):
    brkt = []
    chk = False
    for i in strr:
        if i == '[' or i == '(':
            brkt.append(i)
        elif brkt and ((brkt[-1] == '[' and i == ']') or (brkt[-1] == '(' and i == ')')):
            brkt.pop()
        elif i == ')' or i == ']':
            return 'no'
            chk = True
            break
    if not chk and not brkt:
        return 'yes'
    else:
    return 'no'

strr = input().rstrip()
while strr != '.':
    print(sol(strr))
    strr = input().rstrip()