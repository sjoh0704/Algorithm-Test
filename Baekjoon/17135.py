import sys
from itertools import combinations
read = sys.stdin.readline
N, M, D = map(int ,read().split())
a = []
for _ in range(N):
    a.append(list(map(int, read().split())))

com = list(combinations([i for i in range(M)], 3))


def attack(archer):
    global kill

    killed_list = []
    for i in range(N-1, -1, -1):
        for j in range(M):
            for x in archer:
                if abs(N - i) + abs(x-j) <= D:
                    if area[i][j] == 1:
                        # area[i][j] = 0
                        if [i, j] not in killed_list:
                            killed_list.append([i, j])

    for ky, kx in killed_list:
        area[ky][kx] = 0
    print(killed_list)
    kill += len(killed_list)
    return

def down():
    for i in range(N-1, 0, -1):
        area[i] = area[i-1]
    area[0] = [0] * M

def check():
    for i in range(N):
        for j in range(M):
            if area[i][j] == 1:
                return True
    return False
count = 0
for c in com:
    kill = 0
    area = [item[:] for item in a]
    for _ in range(M+1):
        attack(c)
        down()
    count = max(count , kill)
print(count)

