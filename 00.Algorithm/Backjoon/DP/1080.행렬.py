import sys
input = sys.stdin.readline

def cnvt(a, i, j):
    for ii in range(i,i+3):
        for jj in range(j,j+3):
            a[ii][jj] = 1 - a[ii][jj]

n,m = map(int, input().split())
a,b = [], []
for _ in range(n):
    a.append(list(map(int, list(input().strip()))))
for _ in range(n):
    b.append(list(map(int, list(input().strip()))))

ans = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            cnvt(a,i,j)
            ans += 1

chk = False
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            chk = True
            break

if chk:
    print(-1)
else:
    print(ans)