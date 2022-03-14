import sys
from collections import deque
read = sys.stdin.readline
N, L, R = map(int ,read().split())
area = []
for _ in range(N):
    area.append(list(map(int, read().split())))

dx = [0, 1, 0, -1] # 북 동 남 서
dy = [-1, 0, 1, 0]

def bfs(y, x, visited):
    total = []
    queue = deque()
    queue.append([y, x])

    # 검색하면서, 조건에 맞을 때 total에 넣는다. 
    while queue:
        cy, cx = queue.popleft()
        if visited[cy][cx]:
            continue
        visited[cy][cx] = 1
        total.append([cy, cx])

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0<= nx < N and 0 <= ny < N and L<= abs(area[cy][cx] - area[ny][nx]) <=R:
                  queue.append([ny, nx])
    # 변화가 없으면 
    if len(total) == 1: 
        return False 

    sum = 0
    for ty, tx in total:
        sum += area[ty][tx]
    result = sum//len(total)
    for ty, tx in total:
        area[ty][tx] = result
    return True
    
changed = True
ans = 0 
while changed:
    visited = [[0 for _ in range(N)] for _ in  range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    cnt += 1
    if cnt == 0: ## 바뀌지 않았으면
        changed = False
    else:  ## 바뀌었으면 
        ans += 1
        changed = True

print(ans)