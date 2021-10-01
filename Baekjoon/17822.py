from collections import deque
import sys
read =sys.stdin.readline
N, M, T = map(int ,read().split())
area = []
for _ in range(N):
    area.append(deque(list(map(int ,read().split()))))
way = []
for _ in range(T):
    way.append(list(map(int, read().split())))
print(area)
print(way)
# dir = [1, -1] 
dx = [0, 0, -1 ,1]
dy = [1, -1, 0, 0]
def rotate(x, d, k):
    for i in range(N):
        if (i + 1) % x == 0:
            if d == 0:
                for _ in range(k):
                    tmp = area[i].pop()
                    area[i].appendleft(tmp)
            else:
                for _ in range(k):
                    tmp = area[i].popleft()
                    area[i].append(tmp)

def bfs():
    visit = [[0 for _ in range(M)] for _ in range(N)]
            
    for i in range(N):
        for j in range(M):
            if area[i][j] == 0:
                continue
            target = area[i][j]
            print()
            print("--------------------------------------",target)
            queue = deque([[i, j]])
            while queue:
                print(queue)
                cy, cx = queue.popleft()
                if visit[cy][cx]:
                    continue
                visit[cy][cx] = 1
                for i in range(4):
                    ny = cy + dy[i]
                    nx = cx + dx[i]
                    if ny == N:
                        ny = 0
                    if nx == M:
                        nx = 0
                    if ny == -1:
                        ny = N-1
                    if nx == -1:
                        nx = M-1
                    if area[ny][nx] == target:
                        area[cy][cx] = 0
                        area[ny][nx] = 0
                        queue.append([ny, nx])
for a in area:
    print(a)
print()
rotate(2, 0, 1)
for a in area:
    print(a)
print()
bfs()

for a in area:
    print(a)




    