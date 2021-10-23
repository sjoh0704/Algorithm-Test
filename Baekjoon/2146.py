import sys
from collections import deque
read = sys.stdin.readline
N = int(read())
area = []
for _ in range(N):
    area.append(list(map(int, read().split())))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def coloring(sy, sx, color):
    queue = deque()
    queue.append([sy, sx])
    while queue:
        cy, cx = queue.popleft()
        if visited[cy][cx]:
            continue
        visited[cy][cx] = 1
        area[cy][cx] = color
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<N and 0<=nx<N and area[ny][nx] == 1:
                queue.append([ny, nx])

def bfs(i, j):
    global target
    my_color = area[i][j]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append([i, j, 0])
    while queue:
        cy, cx, cc = queue.popleft()
        if visited[cy][cx]:
            continue
        visited[cy][cx] = 1
        if target < cc:
            continue
        if area[cy][cx] != my_color and area[cy][cx]:
            target = min(target, cc)
            continue
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny<N and 0<=nx<N and (not area[ny][nx] or area[ny][nx] != my_color):
                queue.append([ny, nx, cc + 1])

visited = [[0 for _ in range(N)] for _ in range(N)] 
color = 1
# coloring
for i in range(N):
    for j in range(N):
        if area[i][j] and not visited[i][j]:
            coloring(i, j, color)
            color += 1
# targeting
target = int(1e9)
for i in range(N):
    for j in range(N):
        if area[i][j]:
            bfs(i, j)

print(target-1)