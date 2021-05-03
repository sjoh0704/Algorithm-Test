import sys
read = sys.stdin.readline


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, before=10001):
    global cnt
    if visited[y][x]:
        return
    visited[y][x] = 1


    for i in range(M):
        print(visited[i])
    print()
    # print(y, x)

    if x == N-1 and y == M-1:
        # print("in")
        cnt +=1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx < N and 0 <=ny<M and not visited[ny][nx] and before > area[ny][nx]:
            dfs(nx, ny, area[ny][nx])

    visited[y][x] = 0

M, N = map(int, read().split())
visited = [[0] * N for _ in range(M)]
area = []
for _ in range(M):
    area.append(list(map(int, read().split())))
cnt = 0
dfs(0, 0)
print(cnt)
