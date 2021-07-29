N = int(input())

if N == 1:
    print(0)
elif N == 2 or N == 3:
    print(1)
else:
    dp = [0] * (N+1)
    dp[2], dp[3] = 1, 1
    for i in range(4,N+1):
        if i%3 == 0 and i%2 == 0:
            dp[i] = min(dp[i//2], dp[i//3], dp[i-1]) + 1            
        elif i%3 == 0:
            dp[i] = min(dp[i//3], dp[i-1]) + 1
        elif i%2 == 0:
            dp[i] = min(dp[i//2], dp[i-1]) + 1
        else:
            dp[i] = dp[i-1] + 1

    print(dp[N])