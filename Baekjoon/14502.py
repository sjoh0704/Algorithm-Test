import sys
from collections import deque
from copy import deepcopy

read = sys.stdin.readline
N, M = map(int, read().split())
area = []
dx = [0, 1, 0, -1] # 북 동 남 서 
dy = [-1, 0, 1, 0]
virus_loc = []  ## 초기 바이러스 위치
save_zone_cnts = [] ## 모든 경우 안전 지역 수 모으기 

for i in range(N):
    tmp = list(map(int, read().split()))
    area.append(tmp)
    for j in range(M):
        if tmp[j] == 2:
            virus_loc.append([i, j])

## 바이러스에서 시작 
def bfs(sy, sx, area, visited):
    queue = deque()
    queue.append([sy, sx, 0])
    while queue:
        cy, cx, cc = queue.popleft()
        if area[cy][cx] != 2: ## 바이러스가 아니라면 패스!
            continue

        if visited[cy][cx]: ## 방문했으면 패스!
            continue
        visited[cy][cx] = 1
        
        for i in range(4):
            ny, nx =  cy + dy[i], cx + dx[i]
            if 0<= nx < M and 0 <= ny < N and not area[ny][nx]:
                area[ny][nx] = 2
                queue.append([ny, nx, cc+1])

## 0인 지역의 수 
def count_save_zone(area):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not area[i][j]:
                cnt += 1 
    return cnt

## 벽 만들기 
def createWall(num=0, cy=0):
    if num == 3:
        area_tmp = deepcopy(area)
        visited = [[0 for _ in range(M)] for _ in range(N)]
        for vy, vx in virus_loc:
            bfs(vy, vx, area_tmp, visited)
        save_zone_cnts.append(count_save_zone(area_tmp))
        return 
    
    for i in range(cy, N):
        for j in range(M):
            if not area[i][j]:
                area[i][j] = 1
                createWall(num+1, i)
                area[i][j] = 0

createWall()
print(max(save_zone_cnts))
