import sys
from collections import deque
read = sys.stdin.readline
# 말처럼 이동
h_dx = [-1, -2, -2, -1, 1, 2, 2, 1]
h_dy = [-2, -1, 1, 2, 2, 1, -1, -2]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


k = int(read())
w, h = map(int ,read().split())
area = []
for _ in range(h):
    area.append(list(map(int ,read().split())))

print(area)

def bfs():
    ans = 100000000
    queue = deque()
    queue.append([0, 0, 0, k])
    visited = [[0 for _ in range(w)] for _ in range(h)]
    
    
    while queue:
        cy, cx, cc, ck = queue.popleft()
        if visited[cy][cx]:
            continue
        visited[cy][cx] = 1
        
        if cy == h-1 and cx == w-1:
            ans = min(ans, cc)
            continue
        print(cy ,cx, cc, ck)
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < h and 0<= nx < w:
                queue.append([ny ,nx, cc+1, ck-1])

    return ans
ans = bfs()
print(ans)