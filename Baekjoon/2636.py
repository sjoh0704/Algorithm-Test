import sys
from collections import deque
read = sys.stdin.readline
N, M = map(int, read().split())
area = []
for i in range(N):
    area.append(list(map(int, read().split())))
dx = [0, -1, 0, 1, 1, 1, -1, -1]
dy = [-1, 0, 1, 0, -1, 1, -1, 1]

def bfs(y = 0, x = 0):
    cnt = 0
    queue = deque()
    queue.append([y, x])
    while queue:
        cy, cx = queue.popleft()
        if area[cy][cx] == 1:
            cnt += 1
            area[cy][cx] = 0
            continue

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<= nx < M and 0 <= ny < N and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                queue.append([ny, nx])


    return cnt



v = [[0] * M for _ in range(N)]
cnt = 0
remain = 0
while True:
    visited = [item[:] for item in v]
    cnt += 1
    check = bfs()
    if check == 0:
        cnt -= 1
        break
    else:
        remain = check
print(cnt)
print(remain)