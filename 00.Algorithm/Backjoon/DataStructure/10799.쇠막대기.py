import sys
input = sys.stdin.readline

strs = list(input().strip())
leng = len(strs)
ans, idx, stick = 0,0,0
while idx<leng-2:
    if strs[idx] == '(':
        if strs[idx+1] == ')':
            ans += stick
            idx += 1
        else:
            stick += 1
            ans += 1
    elif strs[idx] == ')':
        stick -= 1
    idx += 1
print(ans)

"""

(())()
2
((())())
5
()(((()())(())()))(())
17
(((()(()()))(())()))(()())
24

"""