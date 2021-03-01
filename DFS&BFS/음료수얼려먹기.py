from collections import deque
import sys
read = sys.stdin.readline
N, M = map(int, read().split())

ice_box = []
for _ in range(N):
    ice_box.append(list(map(int, list(read().strip()))))


def bfs(y, x):
    d = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    queue = deque()
    queue.append([y, x])
    while queue:
        cy, cx = queue.popleft()
        if ice_box[cy][cx] == 0:
            ice_box[cy][cx] = 1

            for i in range(4):
                ny = cy + d[i][0]
                nx = cx + d[i][1]
                if 0 <=nx < M and 0 <= ny < N:
                    if ice_box[ny][nx] == 0:
                        queue.append([ny, nx])

count = 0
for y in range(N):
    for x in range(M):
        if ice_box[y][x] == 0:
            count += 1
            bfs(y, x)
print(count)


