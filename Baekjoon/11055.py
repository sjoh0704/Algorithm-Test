import sys
# read = sys.stdin.readline
# N = int(read().strip())
# sequence = [0] + list(map(int, read().split()))
#
# dp = [0 for _ in range(N+1)]
# dp[-1] = sequence[-1]
# for i in range(N-1, 0, -1):
#     FLAG = True
#     for j in range(i+1, N+1):
#         if sequence[i] < sequence[j]:
#             FLAG = False
#             dp[i] = max(dp[i], dp[j] + sequence[i])
#     if FLAG:
#         dp[i] = max(max(dp[i:]), sequence[i])
# print(dp[1])
n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
dp[0] = a[0]
for i in range(1, n):
    s = []
    for j in range(i - 1, -1, -1):
        if a[i] > a[j]:
            s.append(dp[j])
    if not s:
        dp[i] = a[i]
    else:
        dp[i] = a[i] + max(s)
print(max(dp))