import sys
input = sys.stdin.readline

N = int(input())
wgts = []
for _ in range(N):
    wgts.append(int(input()))

wgts.sort()
max_wgts = [wgts[i]*(N-i) for i in range(N)]
print(max(max_wgts))