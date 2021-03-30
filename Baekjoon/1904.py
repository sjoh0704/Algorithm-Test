import sys
read = sys.stdin.readline
N = int(read().strip())
def sol():
    if N == 1 or N == 2:
        return N
    dp = [0 for _ in range(N+1)]
    dp[1], dp[2] = 1, 2
    for i in range(3, N+1):
        dp[i] =(dp[i-1] + dp[i-2]) % 15746
    return dp[N]
print(sol())
