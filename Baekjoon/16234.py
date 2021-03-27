import sys
read = sys.stdin.readline
N, L, R = map(int, read().split())
country = []
for _ in range(N):
    country.append(list(map(int, read().split())))

def dfs(y, x):
    global move
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    stack = [[y, x]]
    check = []
    sum = 0
    while stack:
        cy, cx = stack.pop()
        if not visit[cy][cx]:
            visit[cy][cx] = 1
            check.append([cy, cx])
            sum += country[cy][cx]
            for d in dir:
                _y = cy + d[0]
                _x = cx + d[1]
                if 0 <= _x < N and 0 <= _y < N and L <= abs(country[_y][_x]-country[cy][cx]) <= R:
                    stack.append([_y, _x])
    aver = sum//len(check)
    for cy, cx in check:
        country[cy][cx] = aver

    if len(check) > 1:
        move = True

global move
move = True
count = 0

while move:
    visit = [[0 for _ in range(N)] for _ in range(N)]
    move = False

    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                dfs(i, j)
    count += 1

print(count-1)
