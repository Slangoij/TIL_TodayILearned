import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = []
for _ in range(k):
    lines.append(int(input()))

l,r = 1, max(lines)

while l<=r:
    c = (l+r)//2
    tmp_n = 0
    for i in range(k):
        tmp_n += lines[i]//c
    
    if tmp_n < n:
        r = c-1
    else:
        l = c+1

print(r)


"""

4 11
802
743
457
539

4 4
1
1
2
2

"""