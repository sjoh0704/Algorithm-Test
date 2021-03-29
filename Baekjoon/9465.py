import sys
read = sys.stdin.readline
T = int(read().strip())

def sol():
    n = int(read().strip())
    sticker = [[0 for _ in range(n+1)]]
    for _ in range(2):
        sticker.append([0] + list(map(int, read().split())))

    dp = [[0 for _ in range(n+1)] for _ in range(3)]
    dp[1][1], dp[2][1] = sticker[2][1], sticker[1][1]
    for i in range(2, n+1):
        dp[1][i] = max(dp[2][i-1], dp[1][i-2], dp[2][i-2])+ sticker[2][i]
        dp[2][i] = max(dp[1][i-1], dp[1][i-2], dp[2][i-2]) + sticker[1][i]
    return max(dp[0][n], dp[1][n], dp[2][n])

for _ in range(T):
    print(sol())