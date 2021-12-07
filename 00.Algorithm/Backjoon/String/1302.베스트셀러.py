import sys
from collections import Counter

selled = Counter()
n = int(input())
for _ in range(n):
    selled.update([input().strip()])

print(sorted(selled.items(), key=lambda x: (-x[-1], x[0]))[0][0])

