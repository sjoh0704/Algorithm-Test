import sys
read = sys.stdin.readline
N = int(read())
M = int(read())
MAX = int(1e9)
cost = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M): 
    s, d, c = map(int, read().split())
    cost[s][d] = c
src, dest = map(int, read().split())
graph = [0 for _ in range(N+1)]
for i in range(N+1):
    if cost[src][i]:
        graph[i] = cost[src][i]
    else:
        graph[i] = MAX
exclude = [src]
while len(exclude) < N:
    min_idx = 0
    for i in range(1, N+1):
        if graph[min_idx] > graph[i] and i not in exclude:
            min_idx = i
    for i, c in enumerate(cost[min_idx]):
        if c:
            graph[i] = min(graph[i], graph[min_idx] + cost[min_idx][i])
    exclude.append(min_idx)
if graph[dest] == MAX:
    print(0)
else:
    print(graph[dest])