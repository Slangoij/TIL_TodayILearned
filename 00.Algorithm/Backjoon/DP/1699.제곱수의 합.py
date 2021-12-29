import math
n = int(input())
dp = [int(1e9)] * (n+1)
dp = [i for i in range(n+1)]

if __name__ == "__main__":
    for i in range(1, n+1):
        if int(math.sqrt(i))**2 == i:
            dp[i] = 1
            continue
        # # 비교 후 할당을 안할 수 있으면 안하는게 시간 절약
        # left = i
        # for j in range(int(math.sqrt(i)), 0, -1):
        #     dp[i] += left//j**2
        #     left %= j**2
        for j in range(1, int(math.sqrt(i))+1):
            if dp[i] > dp[i-j*j]+1:
                dp[i] = dp[i-j*j]+1

    print(dp[n])
