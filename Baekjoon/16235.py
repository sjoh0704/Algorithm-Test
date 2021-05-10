import sys

read = sys.stdin.readline
N, M, K = map(int, read().split())
nut = []
area = [[5]*N for _ in range(N)]
trees = [[[]for _ in range(N)]for _ in range(N)]
location = []
for _ in range(N):
    nut.append(list(map(int, read().split())))
for _ in range(M):
    x, y, age = map(int, read().split())
    trees[y-1][x-1].append(age)

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, -1, 1, 1, -1]

def season():
    for i in range(N):
        for j in range(N):
            if len(trees[i][j]) != 0:
                trees[i][j].sort()
                for k, t in enumerate(trees[i][j]):

                    if t!=0 and area[i][j] >= t:
                        area[i][j] -= t
                        trees[i][j][k] += 1
                    else:
                        area[i][j] += t //2
                        trees[i][j][k] = 0

    for i in range(N):
        for j in range(N):
            if len(trees[i][j]) != 0:
                for k, t in enumerate(trees[i][j]):
                    if t>0 and t % 5 == 0:
                        cx = j
                        cy = i
                        for d in range(8):
                            nx = cx + dx[d]
                            ny = cy + dy[d]
                            if 0<=nx < N and 0<= ny<N:

                                trees[ny][nx].append(1)

    for i in range(N):
        for j in range(N):
            area[i][j] += nut[i][j]

for _ in range(K):
    season()
total = 0
for i in range(N):
    for j in range(N):
        if len(trees[i][j]) != 0:
            for k in trees[i][j]:
                if k != 0:
                    total += 1
print(total)

