import sys
from collections import deque
read = sys.stdin.readline
N = int(read())
board = [deque(map(int, read().split())) for _ in range(N)]

def left():
    for i in range(N):
        for j in range(N-1):
            if board[i][j] == 0:
                for k in range(j+1,N):
                    if board[i][k] != 0:
                        board[i][j], board[i][k] = board[i][k], board[i][j]
        for j in range(N-1):

            if board[i][j] == board[i][j+1]:
                board[i][j] *= 2
                board[i][j+1] = 0
        for j in range(N-1):
            if board[i][j] == 0:
                for k in range(j+1,N):
                    if board[i][k] != 0:
                        board[i][j], board[i][k] = board[i][k], board[i][j]
def right():
    for i in range(N):
        for j in range(N-1, 0, -1):
            if board[i][j] == 0:
                for k in range(0, j):
                    if board[i][k] != 0:
                        board[i][j], board[i][k] = board[i][k], board[i][j]
        for j in range(N-1, 0, -1):

            if board[i][j] == board[i][j-1]:
                board[i][j] *= 2
                board[i][j-1] = 0
        for j in range(N-1, 0, -1):
            if board[i][j] == 0:
                for k in range(0, j):
                    if board[i][k] != 0:
                        board[i][j], board[i][k] = board[i][k], board[i][j]

def up():
    for i in range(N): # x
        for j in range(N-1): # y
            if board[j][i] == 0:
                for k in range(j+1,N):
                    if board[k][i] != 0:
                        board[j][i], board[k][i] = board[k][i], board[j][i]
        for j in range(N-1):

            if board[j][i] == board[j+1][i]:
                board[j][i] *= 2
                board[j+1][i] = 0
        for j in range(N-1):
            if board[j][i] == 0:
                for k in range(j + 1, N):
                    if board[k][i] != 0:
                        board[j][i], board[k][i] = board[k][i], board[j][i]
def down():
    for i in range(N): # x
        for j in range(N-1, 0, -1): # y
            if board[j][i] == 0:
                for k in range(0, j):
                    if board[k][i] != 0:
                        board[j][i], board[k][i] = board[k][i], board[j][i]
        for j in range(N-1, 0, -1):

            if board[j][i] == board[j-1][i]:
                board[j][i] *= 2
                board[j-1][i] = 0
        for j in range(N-1, 0, -1):
            if board[j][i] == 0:
                for k in range(0, j):
                    if board[k][i] != 0:
                        board[j][i], board[k][i] = board[k][i], board[j][i]

dic ={1:up(),2: down(), 3: right(), 4: left()}

cnt = 0
def sol():
    global cnt
    if cnt == 5:
        answer = 0
        for b in board:
            answer = max(answer, max(b))

        print(answer)
    for i in range(1, 5):
        dic[i]
        cnt += 1
        sol()

sol()



for i in range(N):
    print(board[i])
