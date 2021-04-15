from collections import deque
read = input
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
visit_R = [[0 for _ in range(M)] for _ in range(N)]
visit_B = [[0 for _ in range(M)] for _ in range(N)]
visit_B[B[0]][B[1]] = 1
visit_R[R[0]][R[1]] = 1

def sol():

    queue = deque()
    cnt = 0
    queue.append([R[0], R[1], B[0], B[1], cnt])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    while queue:
        print(queue)
        cry, crx, cby, cbx, cc = queue.popleft()

        if cc > 10:
            return -1

        if board[cry][crx] == "O" and board[cby][cbx] != "O":
            return cc
        if board[cry][crx] == "O" and board[cby][cbx] == "O":
            return -1
        for i in range(4):
            nry = cry
            nrx = crx
            nby = cby
            nbx = cbx
            while 1 <= nrx <M-1 and 1<= nry < N-1 and board[nry][nrx] != '#':
                nry += dy[i]
                nrx += dx[i]
                if board[nry][nrx] == "O":
                    break
            else:
                nry -= dy[i]
                nrx -= dx[i]

            while 1 <= nbx < M - 1 and 1 <= nby < N - 1 and board[nby][nbx] != '#':
                nby += dy[i]
                nbx += dx[i]
                if board[nby][nbx] == "O":
                    break
            else:
                nby -= dy[i]
                nbx -= dx[i]

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
            if visit_R[nry][nrx] == 0 or visit_B[nby][nbx] == 0:
                visit_R[nry][nrx] = 1
                visit_B[nby][nbx] = 1
                queue.append([nry, nrx, nby, nbx, cc+1])
    return  -1
print(sol())
