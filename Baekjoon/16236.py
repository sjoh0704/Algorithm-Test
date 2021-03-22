import sys
from collections import deque
read = sys.stdin.readline
N = int(read())
space = []
baby = []
fish = list()
for i in range(N):
    tmp = list(map(int, read().split()))
    space.append(tmp)
    for j in range(N):
        if tmp[j] == 0:
            continue
        elif tmp[j] == 9:
            baby = [i, j]
        else:
            fish.append((tmp[j], i, j))

def find_first(fish_space, y, x, size,):
    dxy = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    queue = deque()
    queue.append([y, x, 0])
    visit = [[0 for _ in range(N)]for _ in range(N)]
    can_eat = []
    while queue:

        cq = queue.popleft()
        # print(cq)
        if not visit[cq[0]][cq[1]]:
            visit[cq[0]][cq[1]] = 1
            if 1 <= fish_space[cq[0]][cq[1]] < size:
                can_eat.append(cq)
                # print(can_eat)


            for d in dxy:
                tmpy = cq[0] + d[0]
                tmpx = cq[1] + d[1]
                if 0 <= tmpx < N and 0 <= tmpy < N and fish_space[tmpy][tmpx] <= size:

                    queue.append([tmpy, tmpx, cq[2] + 1])
    can_eat.sort(key=lambda x:(x[2], x[0], x[1]))

    return can_eat




def sol():

    size = 2
    total_distance = 0
    eat_cnt = 0
    while True:

        tmp = find_first(space, baby[0], baby[1], size)
        if len(tmp) != 0:

            y, x, dist = tmp[0]

            space[baby[0]][baby[1]] = 0
            baby[0] = y
            baby[1] = x

            total_distance += dist
            eat_cnt += 1
            if eat_cnt == size:
                size += 1
                eat_cnt = 0

        else:
            break





        print()
        for i in range(N):
            print(space[i])
        print(total_distance, size)

    print(total_distance)

sol()
