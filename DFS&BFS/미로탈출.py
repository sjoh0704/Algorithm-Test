import sys
read = sys.stdin.readline
N, M = map(int, read().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, list(read().strip()))))
visit = list(maze)

def dfs():
    cnt = 1
    ans = 100000
    d = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    stack = [[0, 0, cnt]]
    while stack:
        cy, cx, cc = stack.pop()
        if cy == N-1 and cx == M-1:
            ans = min(ans, cc)
        if visit[cy][cx] == 1:
            visit[cy][cx] = 0
            for i in range(4):
                nx = cx + d[i][0]
                ny = cy + d[i][1]
                if 0<= ny <N and 0<= nx <M :
                    stack.append([ny, nx, cc+1])
    return ans
print(dfs())







