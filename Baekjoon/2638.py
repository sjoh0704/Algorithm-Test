import sys
from collections import deque
read = sys.stdin.readline
N, M = map(int ,read().split())
area = []
for _ in range(N):
    area.append(list(map(int, read().split())))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def checkEmpty():
    visted = [[0] * M for _ in range(N)]
    visted[0][0] = 1
    queue = deque([[0, 0]])
    while queue:
        cy, cx = queue.popleft()
        if area[cy][cx] == 0:
            area[cy][cx] = -1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<= nx < M and 0 <= ny < N and not visted[ny][nx] and area[ny][nx] != 1:
                visted[ny][nx] = 1
                queue.append([ny, nx])

def bfs():
    visted = [[0] * M for _ in range(N)]
    queue = deque([[0, 0]])
    erase = []
    while queue:
        cy, cx = queue.popleft()
        touch = 0
        if area[cy][cx] == 1:
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 <= nx < M and 0 <= ny < N and area[ny][nx] == -1:
                    touch += 1
                    if touch >= 2:
                        break
            if touch >= 2:
                erase.append([cy, cx])

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<= nx < M and 0 <= ny < N and not visted[ny][nx]:
                visted[ny][nx] = 1
                queue.append([ny, nx])

    if len(erase) == 0:
        return False
    for y, x in erase:
        area[y][x] = -1
    return True
recursion = True
cnt = 0
while recursion:
    cnt += 1
    checkEmpty()
    recursion = bfs()
print(cnt-1)
