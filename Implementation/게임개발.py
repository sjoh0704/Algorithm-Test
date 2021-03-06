from collections import deque
import sys
read = sys.stdin.readline
N, M = map(int, read().split())
sy, sx, dir = map(int, read().split())
jido = []
d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
for _ in range(N):
    jido.append(list(map(int, read().split())))


def sol():
    jido[sy][sx] = 1
    cnt = 1
    queue = deque([[sy, sx, dir, cnt]])

    while queue:
        cy, cx, cd, cc = queue.popleft()
        finish = 0
        while not queue and finish != 4:
            if cd == 0:
                cd = 3
            else:
                cd -= 1

            finish += 1
            ny = cy + d[cd][0]
            nx = cx + d[cd][1]
            if 0 <= ny < N and 0 <= nx < M:
                if jido[ny][nx] == 0:
                    queue.append([ny, nx, cd, cc + 1])
                    jido[ny][nx] = 1
        else:
            cnt = cc

    return cnt

print(sol())








