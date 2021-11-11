import sys
input = sys.stdin.readline

dp = [[[1 for _ in range(21)] for _ in range(21)] for _ in range(21)]


def w(a, b, c):
    if a >= 20 or b >= 20 or c >= 20:
        a, b, c = 20, 20, 20
    for i in range(1, a+1):
        for j in range(1, b+1):
            for k in range(1, c+1):
                if i < j < k:
                    dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
                else:
                    dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]


todo = []
maxa, maxb, maxc = -51, -51, -51
a, b, c = map(int, input().split())
while a != -1 or b != -1 or c != -1:
    todo.append((a, b, c))
    maxa, maxb, maxc = max(a, maxa), max(b, maxb), max(c, maxc)
    a, b, c = map(int, input().split())
w(maxa, maxb, maxc)
for a,b,c in todo:
    tar_a, tar_b, tar_c = a, b, c
    if a <= 0 or b <= 0 or c <= 0:
        tar_a, tar_b, tar_c = 0, 0, 0
    elif a > 20 or b > 20 or c > 20:
        tar_a, tar_b, tar_c = 20, 20, 20
    print(f"w({a}, {b}, {c}) = {dp[tar_a][tar_b][tar_c]}")

"""
20 20 20
19 19 20
-1 -1 -1

w(20, 20, 20) = 1048576
w(19, 19, 20) = 524288
"""