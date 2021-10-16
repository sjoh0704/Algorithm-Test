from collections import deque
import sys
inf = int(1e9)
read = sys.stdin.readline
R, C = map(int, read().split())
area = []
water = []
start = None
for i in range(R):
    tmp = list(read())[:-1]
    print(tmp)
    area.append(tmp)
    for j in range(C):
        if tmp[j] == 'S':
            start = [i, j, 0]
        elif tmp[j] == '*':
            water.append([i, j, 0])
    
print(area)
print(water)
print(start)
queue = deque()
visited = [[[0, 0]for _ in range(C)]for _ in range(R)]
for w in water:
    queue.append(w)
queue.append(start)

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
ans = inf
while queue:
    cy, cx, cc = queue.popleft()
    if area[cy][cx] == '*' and not visited[cy][cx][0]:
        visited[cy][cx][0] = 1
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<= ny < R and 0<= nx < C:
                if area[ny][nx] != 'D' and area[ny][nx] != 'X':
                    area[ny][nx]= '*'
                    queue.append([ny, nx, 0])
    elif area[cy][cx] != 'X' and not visited[cy][cx][1]:
        if area[cy][cx] == 'D':
            ans = min(anx, cc)
            print(ans)

        visited[cy][cx][1] = 1
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<= ny < R and 0<= nx < C:
                if area[ny][nx] != '*' and area[ny][nx] != 'X':
                    area[ny][nx]= '*'
                    queue.append([ny, nx, cc+1])

print(ans)