import sys
read = sys.stdin.readline
n = int(read())
area = []
for _ in range(n):
    area.append(list(map(int, read().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
dy =[0, 0, 1, -1]
dx =[1, -1 ,0, 0]

def dfs(cy, cx, area, visited=[]):
    if dp[cy][cx] == 0:
        dp[cy][cx] = 1
    
    visited.append([cy, cx])
    print(cy, cx)
    
    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]
        if 0 <= ny < n and 0 <= nx < n and [ny, nx] not in visited:
            if area[ny][nx] > area[cy][cx]:
                dfs(ny, nx, area, visited)
                dp[ny][nx] = max(dp[cy][cx] + 1, dp[ny][nx]) 

# dfs(1, 0, area)
for i in range(n):
    for j in range(n):
        _area = area.copy()
        print("--------------------------------")
        dfs(i, j, _area)
        for d in dp:
            print(d)
        print()