import sys
read = sys.stdin.readline
N = int(read())
M = int(read())
MAX = 100000000
cost = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M): 
    s, d, c = map(int, read().split())
    cost[s][d] = c
src, dest = map(int, read().split())

graph = [0 for _ in range(N+1)]

# 초기값 설정
for i in range(N+1):
    if cost[src][i]:
        graph[i] = cost[1][i]
    else:
        graph[i] = MAX
# print(graph)

exclude = [src]
min_idx = 0


while len(exclude) < N:
    # print(graph)
    for i in range(1, N+1):
        if graph[min_idx] > graph[i] and i not in exclude:
            min_idx = i
    
    for i in range(1, N+1):
        if i not in exclude:
            graph[i] = min(graph[i], graph[min_idx] + cost[min_idx][i])

    exclude.append(min_idx)


print(graph[dest])
