import sys
from collections import deque
read = sys.stdin.readline
N = int(read())
space = []
shark_y, shark_x = -1, -1

for i in range(N):
    tmp = list(map(int, read().split()))
    space.append(tmp)
    for j in range(N):
        if tmp[j] == 9:
            shark_y, shark_x = i, j


def find_first(fish_space, y, x, size,):
    dxy = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    queue = deque([[y, x, 0]])
    visit = [[0 for _ in range(N)]for _ in range(N)]
    can_eat = []
    while queue:
        cq = queue.popleft()
        if not visit[cq[0]][cq[1]]:
            visit[cq[0]][cq[1]] = 1
            if 1 <= fish_space[cq[0]][cq[1]] < size:
                can_eat.append(cq)
            for d in dxy:
                _y = cq[0] + d[0]
                _x = cq[1] + d[1]
                if 0 <= _x < N and 0 <= _y < N and fish_space[_y][_x] <= size:
                    queue.append([_y, _x, cq[2] + 1])
    can_eat.sort(key=lambda x: (x[2], x[0], x[1]))
    return can_eat


def sol():
    global shark_x, shark_y
    shark_size = 2
    total_time = 0
    eat_cnt = 0
    while True:
        tmp = find_first(space, shark_y, shark_x, shark_size)
        if len(tmp) == 0:
            break
        _y, _x, time = tmp[0]
        space[_y][_x] = 0
        space[shark_y][shark_x] = 0
        shark_y, shark_x = _y, _x
        total_time += time
        eat_cnt += 1
        if eat_cnt == shark_size:
            shark_size += 1
            eat_cnt = 0
    print(total_time)

sol()
