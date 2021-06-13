import sys
from collections import deque
read = sys.stdin.readline
N = int(read().strip())
K = int(read().strip())
snake = deque([[0, 0]])
area = [[0] * N for _ in range(N)]
for _ in range(K):
    y, x = map(int, read().split())
    area[y-1][x-1] = 1
L = int(read().strip())
dir = []
before_sec = 0
for _ in range(L):
    sec, d = read().split()
    dir.append([int(sec) - before_sec, d])
    before_sec = int(sec)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def move(sec=100, dir=0):
    global count
    for i in range(sec):
        head = snake[0]
        ny = head[0] + dy[dir]
        nx = head[1] + dx[dir]
        count += 1
        if 0 > nx or nx >= N or 0 > ny or ny >= N or [ny, nx] in snake:
            return False
        snake.appendleft([ny, nx])
        if area[ny][nx] == 1:
            area[ny][nx] = 0
        else:
            snake.pop()
    return True

def findDir(base_dir, which_dir):
    if which_dir == 'D':
        base_dir += 1
        if base_dir == 4:
            base_dir = 0
    else:
        base_dir -= 1
        if base_dir == -1:
            base_dir = 3
    return base_dir

next_dir = 0
count = 0
FLAG = True
i = 0
while FLAG:
    if i < len(dir):
        FLAG = move(dir[i][0], next_dir)
        next_dir = findDir(next_dir, dir[i][1])
    else:
        FLAG = move(dir=next_dir)
    i += 1
print(count)