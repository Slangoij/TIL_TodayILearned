import sys
import copy
input = sys.stdin.readline

n = int(input())
mapforhor = [list(input().strip()) for _ in range(n)]
mapforver = copy.deepcopy(mapforhor)
for i in range(n)
    j = 0
    while j < n:
        if mapforhor[i][j] == '.':
            stt = j
            while mapforhor[i][j] == '.' and j<n:
                j += 1
            if j - stt >= 2:

