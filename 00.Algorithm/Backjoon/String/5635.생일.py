import sys
from datetime import datetime
input = sys.stdin.readline

n = int(input())
bds = []
for _ in range(n):
    strs = input().split()
    name, dd, mm, yyyy = strs[0], int(strs[1]), int(strs[2]), int(strs[3])
    bds.append([name, datetime(yyyy, mm, dd)])
bds.sort(key=lambda x: x[-1])
print(bds[-1][0], bds[0][0], sep='\n')
