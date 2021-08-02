import sys
input = sys.stdin.readline

N,M = map(int, input().split())

maxx, minn = max(N,M), min(N,M)

if maxx%2 ==1 and minn%2==1:
    print('B')
else:
    print('A')