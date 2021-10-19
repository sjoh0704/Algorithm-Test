import sys
from collections import deque
read = sys.stdin.readline
r, c = map(int ,read().split())
area = []
for _ in range(r):
    area.append(list(read())[:-1])
# print(area)

visited = [[ 0 for _ in range(c)]for _ in range(r)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]


def bfs(sy, sx):
    global target 
    queue = deque([[sy, sx, 1]])
    while queue:
        cy, cx, cc = queue.popleft()    
        if visited[cy][cx]:
            continue
        target = max(target, cc)
        visited[cy][cx] = 1
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<=ny <r and 0<=nx < c:
                if area[ny][nx] == 'L':
                    queue.append([ny, nx, cc+1])

                

target = 0
for i in range(r):
    for j in range(c):
        if area[i][j] == 'L' and not visited[i][j]:
            # print(i, j)
            bfs(i, j)
            # print(target)
print(target)