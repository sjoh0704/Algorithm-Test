import sys
from heapq import heappush, heappop
read = sys.stdin.readline
N = int(read())
M = int(read())
cost = [[] for _ in range(N+1)]
inf = int(1e9)
for _ in range(M):
    s, e, v = map(int, read().split())
    cost[s].append([e, v])
start, end = map(int ,read().split())
def dijkstra(start, end):
    dp = [inf for _ in range(N+1)]
    dp[start] = 0
    hq = []
    heappush(hq, [0, start])
    while hq:
        cv, ce = heappop(hq)
        if dp[ce] < cv:
            continue
        for ne, nv in cost[ce]:
            if dp[ne] > dp[ce] + nv:
                dp[ne] = dp[ce] + nv
                heappush(hq, [dp[ne], ne])
    print(dp[end])
dijkstra(start, end)
