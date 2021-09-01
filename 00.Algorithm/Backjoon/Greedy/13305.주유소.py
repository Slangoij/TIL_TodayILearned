import sys
input = sys.stdin.readline

N = int(input())
roads = list(map(int, input().split()))
prcs = list(map(int, input().split()))
# roads.reverse()
# prcs.reverse()

ans = 0
tmproad, tmprice = 0, prcs[0]
for i in range(len(roads)):
    tmproad += roads[i]
    if tmprice > prcs[i+1]:
        ans += tmproad * tmprice
        tmprice = prcs[i+1]
        tmproad = 0
ans += tmproad * tmprice

print(ans)

"""

4
2 3 1
5 2 4 1

4
3 3 4
1 1 1 1

"""