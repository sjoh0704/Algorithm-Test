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
    cnt = 0
    for i in range(N):
        for j in range(M):
            if area[i][j] == 0:
                continue
            target = area[i][j]
            queue = deque([[i, j]])
            while queue:
                cy, cx = queue.popleft()
                for k in range(4):
                    ny = cy + dy[k]
                    nx = cx + dx[k]
                    if ny == N or ny == -1:
                        continue
                    if nx == M:
                        nx = 0
                    if nx == -1:
                        nx = M-1
                    if area[ny][nx] == target:
                        cnt += 1
                        area[cy][cx] = 0
                        area[ny][nx] = 0
                        queue.append([ny, nx])
    if cnt == 0:
        total = 0
        count = 0
        for i in range(N):
            for j in range(M):
                if area[i][j]:
                    total += area[i][j] 
                    count += 1
        if count != 0:
            avg = total/count
            for i in range(N):
                for j in range(M):
                    if area[i][j] > avg:
                        area[i][j] -= 1
                    elif 0 < area[i][j] < avg:
                        area[i][j] += 1

for x, d, k in way:
    rotate(x, d, k)
    bfs()
ans = 0
for i in range(N):
    for j in range(M):
        ans += area[i][j]
print(ans)
