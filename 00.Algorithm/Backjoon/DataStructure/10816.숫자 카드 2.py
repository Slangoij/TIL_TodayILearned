from collections import Counter
n = int(input())
lst = list(map(int, input().split()))
cnts = Counter(lst)
m = int(input())
todolst = list(map(int, input().split()))
ans = []
for todo in todolst:
    ans.append(cnts[todo])
print(" ".join(map(str, ans)))