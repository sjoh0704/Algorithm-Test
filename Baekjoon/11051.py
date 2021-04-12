import sys
read = sys.stdin.readline
N, K = map(int, read().split())
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
dp[1][0], dp[1][1] = 1, 1

for n in range(2, N+1):
    for k in range(0, n+1):
        dp[n][k] = (dp[n - 1][k] + dp[n - 1][k - 1]) % 10007

print(dp[N][K])