from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(i, j, char):
    q = deque()
    q.append([i, j])
    chain = []
    chain.append([i, j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 12 and 0 <= ny < 6 and visit[nx][ny] == 0 and s[nx][ny] == char:
                visit[nx][ny] = 1
                q.append([nx, ny])
                chain.append([nx, ny])
    if len(chain) > 3:
        for x, y in chain:
            s[x][y] = "."
        return True
    return False
def down():
    for i in range(6):
        for j in range(10, -1, -1):
            for k in range(11, j, -1):
                if s[j][i] != "." and s[k][i] == ".":
                    s[k][i] = s[j][i]
                    s[j][i] = "."
                    break
s = [list(input().strip()) for i in range(12)]
result = 0

while True:
    FLAG = False
    visit = [[0] * 6 for i in range(12)]
    for i in range(12):
        for j in range(6):
            if s[i][j] != "." and visit[i][j] == 0:
                visit[i][j] = 1
                if FLAG:
                    bfs(i, j, s[i][j])
                else:
                    FLAG = bfs(i, j, s[i][j])

    if not FLAG:
        break
    down()
    result += 1
print(result)