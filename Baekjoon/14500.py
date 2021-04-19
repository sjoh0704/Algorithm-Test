import sys
read = sys.stdin.readline
N, M = map(int ,read().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, read().split())))

def tetromino1():
    dy = [[0, 0, 0, 0], [0, 1, 2, 3]]
    dx = [[0, 1, 2, 3], [0, 0, 0, 0]]
    return [dy, dx]

def tetromino2():
    dy = [[0, 0, 1, 1]]
    dx = [[0, 1, 1, 0]]
    return [dy, dx]

def tetromino3():
    dy = [[0, 1, 2, 2], [0, 0, 0, -1], [0, 0, 1, 2],[0, 0, 0, 1], [0, 0, -1, -2],[0, 1, 1, 1], [0, 0, 1, 2],[0, 0, 0, 1]]
    dx = [[0, 0, 0, 1], [0, 1, 2, 2], [0, 1, 1, 1],[0, 1, 2, 0], [0, 1, 1, 1],[0, 0, 1, 2], [0, 1, 0, 0],[0, 1, 2, 2]]
    return [dy, dx]

def tetromino4():
    dy = [[0, 1, 1, 2], [0, 0, -1, -1], [0, 1, 0, -1], [0, 0, 1, 1]]
    dx = [[0, 0, 1, 1], [0, 1, 1, 2], [0, 0, 1, 1], [0, 1, 1, 2]]
    return [dy, dx]

def tetromino5():
    dy = [[0, 0, 0, 1], [0, 0, -1, 1], [0, 0, 0, -1], [0, 0, 1, -1]]
    dx = [[0, -1, 1, 0], [0, 1, 0, 0], [0, -1, 1, 0], [0, -1, 0, 0]]
    return [dy, dx]


dy = tetromino1()[0] + tetromino2()[0] + tetromino3()[0] + tetromino4()[0] + tetromino5()[0]
dx = tetromino1()[1] + tetromino2()[1] + tetromino3()[1] + tetromino4()[1] + tetromino5()[1]
total_max = 0
for i in range(N):
    for j in range(M):
        for d in range(len(dx)):
            tmp_max = 0
            FLAG = True
            for k in range(4):
                if 0<=i+dy[d][k]<N and 0<=j+dx[d][k]<M:
                    tmp_max += maps[i+dy[d][k]][j+dx[d][k]]
                else:
                    FLAG = False
                    break
            if FLAG:
                total_max = max(total_max, tmp_max)
print(total_max)