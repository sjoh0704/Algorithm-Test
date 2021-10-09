import sys
# sys.setrecursionlimit(10**6)
read = sys.stdin.readline
n = int(read())
graph = []
for _ in range(n):
    graph.append(list(map(int ,read().split())))
dp = [[0 for _ in range(n)] for _ in range(n)]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
def dfs(y, x):
    if dp[y][x]:
        return dp[y][x]
    dp[y][x] = 1
    # visited.append([y,x])
    # print(y, x)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<= nx < n and 0 <= ny < n :
            if graph[ny][nx] > graph[y][x]:
                # pdb.set_trace()
                dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)
    return dp[y][x]
    
result = 0
for i in range(n):
    for j in range(n):
        # print(i, j, "------------------")
        result = max(result, dfs(i, j))
        # for d in dp:
        #     print(d)
        # print()
print(result)