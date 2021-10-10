import sys
from collections import deque
read = sys.stdin.readline
# 말처럼 이동
MAX = 10000000
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


def bfs():
    ans = MAX
    queue = deque()
    queue.append([0, 0, 0, k])
    visited = [[[0 ,0] for _ in range(w)] for _ in range(h)]
    visited[0][0] = [1, 1]
    while queue:
        cy, cx, cc, ck = queue.popleft()
        # print(cy, cx, cc, ck)
        if cy == h-1 and cx == w-1:
            ans = min(ans, cc)
            continue
        # print(cy ,cx, cc, ck)

        if ck > 0:
            _ck = ck - 1
            for i in range(8):
                ny = cy + h_dy[i]
                nx = cx + h_dx[i]
                if 0 <= ny < h and 0<= nx < w and not area[ny][nx] and not visited[ny][nx][0]:
                    queue.append([ny ,nx, cc+1, _ck])
                    visited[ny][nx][0] = 1
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < h and 0<= nx < w and not area[ny][nx] and not visited[ny][nx][1]:
                queue.append([ny ,nx, cc+1, ck])
                visited[ny][nx][1] = 1

    return ans
ans = bfs()
if ans == MAX:
    print(-1)
else:
    print(ans)