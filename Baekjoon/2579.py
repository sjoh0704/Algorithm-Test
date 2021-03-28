import sys
read = sys.stdin.readline
N = int(read().strip())
steps = [0 for _ in range(N+1)]
for i in range(1, N+1):
    steps[i] = int(read().strip())

def top(N):
    if N == 1:
        print(steps[1])
        return
    dp = [[0 for _ in range(N + 1)] for _ in range(3)]
    dp[1][1], dp[2][2], dp[1][2] = steps[1], steps[2], steps[1] + steps[2]
    for i in range(3, N+1):
        dp[1][i] = steps[i] + dp[2][i-1]
        dp[2][i] = steps[i] + max(dp[2][i-2], dp[1][i-2])
    print(max(dp[1][N], dp[2][N]))

top(N)