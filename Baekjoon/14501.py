import sys
read = sys.stdin.readline
N = int(read().strip())
t = []
p = []
for _ in range(N):
    tmp_t, tmp_p = map(int ,read().split())
    t.append(tmp_t)
    p.append(tmp_p)

dp = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    if t[i] + i <= N:
        dp[i] = max(dp[i+1], dp[i+t[i]] + p[i])
    else:
        dp[i] = dp[i+1]
print(dp[0])











# for i in range(N-1, -1, -1):
#     if t[i] + i > N:
#         dp[i] = dp[i+1]
#     else:
#         dp[i] = max(dp[i+1], p[i] + dp[i + t[i]])
# print(dp[0])

