import sys
read = sys.stdin.readline
n = int(read())
area = []
for _ in range(n):
    area.append(list(map(int, read().split())))

dy =[0, 0, 1, -1]
dx =[1, -1 ,0, 0]

def dfs(sy, sx, area):
    global target
    stack = [[sy, sx, 1]]
    visit = [[0 for _ in range(n)] for _ in range(n)]
    while stack:
        cy, cx, cc = stack.pop()
        target = max(target, cc) 
        # print(cy, cx)
        if visit[cy][cx]:
            continue
        visit[cy][cx] = 1
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<= ny < n and 0<=nx <n:
                if area[cy][cx] < area[ny][nx]:
                    stack.append([ny, nx, cc+1])
target = 0
for i in range(n):
    for j in range(n):
        _area = area.copy()
        dfs(i, j, _area)
print(target)