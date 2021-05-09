import heapq
import sys
read = sys.stdin.readline
N, M, K = map(int, read().split())
nut = []
area = [[5]*N for _ in range(N)]
trees = []
for _ in range(N):
    nut.append(list(map(int, read().split())))
for _ in range(M):
    x, y, age = map(int, read().split())
    heapq.heappush(trees, [age, y-1, x-1])
dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, -1, 1, 1, -1]

def season():

    for i, tmp in enumerate(trees):
        ca, cy, cx = tmp
        if area[cy][cx] >= ca:
            area[cy][cx] -= ca
            trees[i][0] += 1
        else:
            area[cy][cx] += trees[i][0] //2
            trees[i][0] = -1
            heapq.heappop(trees)

    for ca, cy, cx in trees:
        if ca % 5 == 0:
            for i in range(8):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0<=nx < N and 0<= ny<N:

                    trees.append([1, ny, nx])

    for i in range(N):
        for j in range(N):
            area[i][j]+= nut[i][j]

for _ in range(K):
    season()
print(len(trees))

