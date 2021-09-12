import sys
import copy
from itertools import combinations
from collections import deque
read = sys.stdin.readline
N, M = map(int,read().split())
area = []
virus = []
for i in range(N):
    tmp = list(map(int, read().split()))
    area.append(tmp)
    for j in range(N):
        if tmp[j] == 2:
            area[i][j] = "*"
            virus.append([i, j, 0])
        elif tmp[j] == 1:
            area[i][j] = "-"

select = list(combinations(virus, M))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def sol(a, virus):
    visit = [[0] * N for _ in range(N)]
    queue = deque(virus)
    max_sec = 0
    while queue:

        cqy, cqx, cqc = queue.popleft()
        if visit[cqy][cqx]:
            continue
        visit[cqy][cqx] = 1
        if str(a[cqy][cqx]).isdigit():
            max_sec = max(max_sec, a[cqy][cqx])
        

        if not (a[cqy][cqx] == "**" or (str(a[cqy][cqx]).isdigit() and a[cqy][cqx])):
            continue
            
        
        for i in range(4):

            ny = cqy + dy[i]
            nx = cqx + dx[i]
            if 0<=nx < N and 0<= ny < N:
                if a[ny][nx] != "**" and a[ny][nx] != "-":
                    if not a[ny][nx]:
                        a[ny][nx] = cqc + 1
                    elif a[ny][nx] == "*":
                        a[ny][nx] = "**"
                    queue.append([ny,nx, cqc+1])
    
 
    for i in range(N):
        for j in range(N):
            if a[i][j] == 0:
                return -1
  
    return max_sec


ans = 100000000
for s in select:
    _area = copy.deepcopy(area)
    for v in s:
        _area[v[0]][v[1]] = "**" # 바이러스 활성화 
    tmp =  sol(_area, s)
    if tmp == -1:
        continue
    ans = min(ans,tmp)

if ans == 100000000:
    print(-1)
else:
    print(ans)
