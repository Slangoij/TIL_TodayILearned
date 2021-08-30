import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    strr = input().strip()
    if len(strr)%2:
        print('NO')
    else:
        chk = False
        stac = 0
        for let in strr:
            if let == '(':
                stac += 1
            elif stac == 0:
                chk = True
                break
            else:
                stac -= 1
        if chk or stac:
            print('NO')
        else:
            print('YES')

"""

6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
    
1
(((()())()

3
((
))
())(()

"""