import sys
from collections import deque
read = sys.stdin.readline
field = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
kind1 = [[[0, 0],[1, 0],[2, 0],[3, 0]],[[0, 0],[0, -1],[0, -2],[0, -3]]]
kind2 = [[[0, 0],[-1, 0],[1, 0],[0, -1]],[[0, 0],[1, 0],[0, -1],[0, 1]],[[0, 0],[-1, 0],[1, 0],[0, 1]],[[0, 0],[-1, 0],[0, 1],[0, -1]]]
kind3 = [[[0, 0],[1, 0],[1, -1],[0, -1]]]
kind4 = [[[0, 0],[-1, 0],[-2, 0],[0, -1]],[[0, 0],[1, 0],[0, -1],[0, -2]], [[0, 0],[-1, 0],[0, 1],[0, 2]],[[0, 0],[0, -1],[1, 0],[2, 0]], [[0, 0],[1, 0],[0, 1],[0, 2]],[[0, 0],[1, 0],[2, 0],[0, 1]],[[0, 0],[-1, 0],[-2, 0],[0, 1]],[[0, 0],[-1, 0],[0, -1],[0, -2]]]
explosion = kind1 + kind2 + kind3 + kind4
for _ in range(12):
    field.append(list(read().strip()))

def find():
    for i in range(6):
        if field[-1][i] != ".":
            # print(i, 11)
            return [i, 11]
    return []

def bfs(start):
    visited = [start]
    queue = deque()
    queue.append(start)
    while queue:
        cx, cy = queue.popleft()
        tmp = field[cy][cx]

        if tmp != '.':
            for e in explosion:
                FLAG = True
                for i in range(0, 4):
                    nx = cx + e[i][0]
                    ny = cy + e[i][1]
                    # print(nx ,ny)
                    if 0 > nx or nx >= 6 or 0 > ny or ny >= 12:
                        FLAG = False
                        break
                    elif tmp != field[ny][nx]:
                        FLAG = False
                        break

                if FLAG:
                    for i in range(4):
                        nx = cx + e[i][0]
                        ny = cy + e[i][1]
                        field[ny][nx] = '.'
                    break

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0<= nx < 6 and 0 <= ny <12:
                if [nx, ny] not in visited:
                    visited.append([nx, ny])
                    queue.append([nx, ny])
def down():
    for i in range(12):
        for j in range(6):
            if field[j]

bfs(find())
for i in range(12):
    print(field[i])
#
# bfs(find())
# for i in range(12):
#     print(field[i])