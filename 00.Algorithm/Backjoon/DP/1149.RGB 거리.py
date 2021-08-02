import sys
input = sys.stdin.readline

N = int(input())
costs = []
for _ in range(N):
    costs.append(list(map(int, input().split())))

dp = [costs[0]]
for i in range(1,N):
    tmp_rgb = []
    for j in range(3):
        tmp = []
        for k in range(3):
            if j != k:
                tmp.append(dp[i-1][k])
        tmp_rgb.append(min(tmp) + costs[i][j])
    dp.append(tmp_rgb)

print(min(dp[-1]))

# 최소값 설정하는 부분에서 각 값의 최대값으로 1000인 것을 
# 10000으로 초기화한 값에 갱신시키는 바람에 부분합의 한계 때문에
# 뒤로 갈수록 커지는 값을 갱신하지 못한 실수
"""

3
26 40 83
49 60 57
13 89 99

2
1 2 3
4 5 6

"""