import sys
from collections import deque
read = sys.stdin.readline
N, M = map(int, read().split())
sea = []
for _ in range(N):
    sea.append(list(map(int, read().split())))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(y, x):

    q = deque()
    q.append([y, x])
    v[y][x] = 1
    while q:

        cy, cx = q.popleft()

        tmp = 0
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<=nx<M and 0 <=ny<N and not v[ny][nx]:
                if sea[ny][nx] == 0:
                    tmp += 1
                else:
                    v[ny][nx] = 1
                    q.append([ny, nx])

        if sea[cy][cx] - tmp <0:
            sea[cy][cx] = 0
        else:
            sea[cy][cx] -= tmp
answer = 0
FLAG = True
visited = [[0] * M for _ in range(N)]
while FLAG:
    v = [item[:] for item in visited]
    tmp = 0
    answer += 1
    for i in range(1, N-1):
        if FLAG:
            for j in range(1, M-1):
                if not v[i][j] and sea[i][j] != 0:

                    tmp += 1
                    bfs(i, j)
                if tmp >= 2:
                    FLAG = False
                    break
        else:
            break
print(answer-1)