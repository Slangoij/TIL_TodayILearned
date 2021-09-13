import sys
input = sys.stdin.readline

def getrt(rts, a):
    if rts[a] == a:    
        return a
    rts[a] = getrt(rts, rts[a])
    return getrt(rts, rts[a])

def union(rts, a, b):
    a = getrt(rts, a)
    b = getrt(rts, b)
    rts[max(a,b)] = min(a,b)

n = int(input())
rts = [i for i in range(n+1)]
k = int(input())
for _ in range(k):
    a,b = map(int, input().split())
    union(rts, a, b)

answer = 0
for i in range(2,n+1):
    if getrt(rts, i) == 1:
        answer += 1

print(answer)