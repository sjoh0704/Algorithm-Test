import sys
read = sys.stdin.readline
N, M = map(int, read().split())
area = []
for i in range(N):
    area.append(list(map(int, read().split())))
dx = [0, -1, 0, 1, 1, 1, -1, -1]
dy = [-1, 0, 1, 0, -1, 1, -1, 1]
visited = [[0]*M for _ in range(N)]
def dfs(cy, cx):
    if visited[cy][cx] == 1:
        return

    visited[cy][cx] = 1
    FLAG = False
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0<= nx < M and 0<= ny < N and area[ny][nx] == 0:
            FLAG = True
            break
    if not FLAG:
        return
    print(cy, cx)
    for i in range(8):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 1<= nx < M-1 and 1<= ny < N-1 and area[ny][nx] == 1:
            dfs(ny, nx)

dfs(3, 1)




