import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)
ans = 0
upp,loww = None, None
for i in range(n):
    if lst[i] > 1:
        if not upp:
            upp = lst[i]
        else:
            ans += lst[i]*upp
            upp = None
    else:
        break
lst.sort()
for i in range(n):
    if lst[i] < 0:
        if not loww:
            loww = lst[i]
        else:
            ans += lst[i]*loww
            loww = None
    else:
        break
if upp:
    ans += upp
if loww and not (loww == -1 and 0 in lst):
    ans += loww
ans += lst.count(1)

print(ans)

"""

6
-5
-2
-1
0
3
6

7
-5
-2
-1
0
1
3
6

6
1
1
0
-1
-1
-1

"""