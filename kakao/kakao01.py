from collections import deque
import sys

def bfs(board, y, x, ty, tx):
    if y == ty and x == tx:
        return 0

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    cnt = 0
    queue = deque([[y, x, cnt]])

    visit = [[0]*4 for _ in range(4)]
    visit[y][x] = 1
    purpose = sys.maxsize

    while queue:
        cy, cx, cc = queue.popleft()
        if cy == ty and cx == tx:
            purpose = min(purpose, cc)

        for i in range(4):
            ny = cy
            nx = cx
            while 0<=ny<4 and 0<= nx < 4:
                ny += dy[i]
                nx += dx[i]
                if 0<=ny<4 and 0<= nx < 4 and board[ny][nx] == 0:
                    continue
                elif 0<=ny<4 and 0<= nx < 4 and board[ny][nx] != 0:
                    break
                else:
                    ny -= dy[i]
                    nx -= dx[i]
                    break

            if not visit[ny][nx]:
                visit[ny][nx] = 1
                queue.append([ny, nx, cc+1])

            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0<=nx<4 and 0<= ny<4:
                if not visit[ny][nx]:
                    visit[ny][nx] = 1
                    queue.append([ny, nx, cc + 1])


    return purpose


def find(board, cnt, selected_card, r, c, selectFlag = False):
    global minValue
    ContinueFlag = False
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                ContinueFlag = True
                break

    if minValue <= cnt:
        return

    if not ContinueFlag:
        minValue = min(minValue, cnt)
        return
    for card in selected_card:
        if not selectFlag:
            tmp = bfs(board, r, c, card[0], card[1])
            tmp += 1
            find(board, cnt+tmp, selected_card, card[0], card[1], True)
        else:
            if (card[0]!= r or card[1] != c) and card[2] == board[r][c]:
                tmp = bfs(board, r, c, card[0], card[1])
                tmp += 1
                board_tmp = board[r][c], board[card[0]][card[1]]
                board[r][c], board[card[0]][card[1]] = 0, 0
                find(board, cnt + tmp, selected_card, card[0], card[1], False)
                board[r][c], board[card[0]][card[1]] = board_tmp


def solution(board, r, c):
    global minValue
    minValue = sys.maxsize
    selected_card = []
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                selected_card.append([i, j, board[i][j]])

    cnt = 0
    find(board, cnt, selected_card, r, c)

    return minValue

print(solution([[0,0,0,0],[1,2,1,2],[0,0,0,0],[0,0,0,0]], 3, 2))