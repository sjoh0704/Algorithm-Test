import sys
read = sys.stdin.readline
M, N = map(int, read().split())
area = []
for _ in range(M):
    area.append(list(map(int, read().split())))

dp = [[-1]*N for _ in range(M)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# dfs와 dp를 이용한다
# 방문한 지역이라면 dp에서 값을 가져오고 그렇지 않다면 dfs로 값을 찾는다.
# dp[b][a] =  (a, b)에서 (N-1, M-1)까지의 내리막길 경로 수
def dfs(x, y):
    if x== N-1 and y == M-1:   # 경로가 있는 경우
        return 1
    if dp[y][x] != -1:   # 방문한 경우
        return dp[y][x]
    else:  # 방문하지 않은 경우
        dp[y][x] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and area[y][x] > area[ny][nx]:  # 내리막길 조건
                dp[y][x] += dfs(nx, ny)
        return dp[y][x]

print(dfs(0, 0))  # (0, 0)에서 (N-1, M-1)까지의 내리막길 경로 수