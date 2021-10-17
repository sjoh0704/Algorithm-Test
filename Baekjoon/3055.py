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
  
    area.append(tmp)
    for j in range(C):
        if tmp[j] == 'S':
            start = [i, j, 'S']
        elif tmp[j] == '*':
            water.append([i, j, '*'])
    
queue = deque()
cnt = deque()
# visited = [[ 0 for _ in range(C)]for _ in range(R)]
visited = []
for w in water:
    queue.append(w)
queue.append(start)
cnt.append(0)
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]
ans = inf
while queue:
    cy, cx, ch= queue.popleft()
    # print(cy, cx, cc)
    
    if ch == '*':
        # print('*',cy, cx, cc)
        # print(queue)
        area[cy][cx]= '*'
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<= ny < R and 0<= nx < C:
                if area[ny][nx] != 'D' and area[ny][nx] != 'X' and area[ny][nx] != '*':
                    queue.append([ny, nx, '*'])
                


    elif ch =='S' and [cy,cx] not in visited:
        cc = cnt.popleft()
        # print(cnt)
        # print('s',cy, cx, cc)
        # print(queue)
        if area[cy][cx] == '*':
            continue


        if area[cy][cx] == 'D':
            ans = min(ans, cc)
            # print(ans)

        visited.append([cy,cx])
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0<= ny < R and 0<= nx < C:
                if area[ny][nx] != '*' and area[ny][nx] != 'X':
                    
                    queue.append([ny, nx, 'S'])
                    cnt.append(cc+1)
    else:
        cc = cnt.popleft()

if ans == inf:
    print('KAKTUS')
else:
    print(ans)