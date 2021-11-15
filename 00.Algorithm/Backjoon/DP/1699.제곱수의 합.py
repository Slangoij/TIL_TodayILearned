import math
n = int(input())
dp = [int(1e9)] * (n+1)


def issqr(num):
    for i in range(1, int(math.sqrt(num))+1):
        if i**2 == num:
            return True
    return False


if __name__ == "__main__":
    for i in range(1, n+1):
        if issqr(i):
            dp[i] = 1
        else:
            for j in range(1, i//2 + 1):
                dp[i] = min(dp[i], dp[j] + dp[i-j])

    print(dp[n])
