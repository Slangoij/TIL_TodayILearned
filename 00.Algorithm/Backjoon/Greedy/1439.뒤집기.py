import sys
input = sys.stdin.readline

S = input().strip()
ans = 0
now = S[0]
for i in range(1,len(S)):
    if now != S[i]:
        now = S[i]
        ans += 1

print((ans+1)//2)