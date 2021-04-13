N = int(input())
dp = [0 for _ in range(N+1)]
try:
    dp[0], dp[2] = 1, 3
    for i in range(2, N//2+1):
        dp[2*i] = dp[2*(i-1)] * 3
        for j in range(2, i+1):
            dp[2 * i] += dp[2 * (i - j)] * 2
except IndexError:
    print(0)
else:
    print(dp[N])
