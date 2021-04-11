import sys
read = sys.stdin.readline
N = int(read().strip())
num = [0] + list(map(int, read().split()))
dp = [1 for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, i):
        if num[i-j] > num[i]:
            dp[i] = max(dp[i], dp[i-j] + 1)
print(max(dp))