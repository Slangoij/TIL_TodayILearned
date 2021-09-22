import sys
input = sys.stdin.readline

n,m = map(int, input().split())
deod = {}
ans = []
for _ in range(n):
    dd = input().strip()
    deod[dd] = False
for _ in range(m):
    bo = input().strip()
    if bo in deod:
        ans.append(bo)
ans.sort()
print(len(ans))
for an in ans:
    print(an)