import sys
from collections import deque
read = sys.stdin.readline
N, M = map(int, read().split())
board = []
R, B =[], []
for i in range(N):
    board.append(list(read().strip()))
    for j in range(M):
        if board[i][j] == 'R':
            R = [i, j]
        if board[i][j] == 'B':
            B = [i, j]


visit= [[[[0] * M for _ in range(N)]for _ in range(M)]for _ in range(N)]
visit[B[0]][B[1]][R[0]][R[1]] = 1

def sol():

    queue = deque()
    cnt = 0
    queue.append([R[0], R[1], B[0], B[1], cnt])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:

        cry, crx, cby, cbx, cc = queue.popleft()

        if cc > 10:
            return -1

        # 빨간색공이 빠지고, 파란색공이 안빠지는 경우 성공
        if board[cry][crx] == "O" and board[cby][cbx] != "O":
            return cc

        # 파란색공이 빠진 경우
        elif board[cby][cbx] == "O":
            continue

        for i in range(4):
            nry = cry
            nrx = crx
            nby = cby
            nbx = cbx

            # 빨간공 먼저
            while 1 <= nrx <M-1 and 1<= nry < N-1 and board[nry][nrx] != '#':
                nry += dy[i]
                nrx += dx[i]
                if board[nry][nrx] == "O":
                    break
            else:
                nry -= dy[i]
                nrx -= dx[i]


            # 다음 파란공
            while 1 <= nbx < M - 1 and 1 <= nby < N - 1 and board[nby][nbx] != '#':
                nby += dy[i]
                nbx += dx[i]
                if board[nby][nbx] == "O":
                    break
            else:
                nby -= dy[i]
                nbx -= dx[i]

            # 빨간공과 파란공이 같은 위치에 있을 경우 처리
            if not (board[nry][nrx] == "O" and board[nby][nbx] == "O"):
                if nrx == nbx and nry == nby:
                    red_diantce = abs(nrx-crx) + abs(nry - cry)
                    blue_diantce = abs(nbx - cbx) + abs(nby - cby)
                    if red_diantce < blue_diantce:
                        nby -= dy[i]
                        nbx -= dx[i]
                    else:
                        nry -= dy[i]
                        nrx -= dx[i]
            if visit[nry][nrx][nby][nbx] == 0:
                visit[nry][nrx][nby][nbx] = 1
                queue.append([nry, nrx, nby, nbx, cc+1])

    # 갈곳이 없어서 멈추는 경우
    return -1
print(sol())
