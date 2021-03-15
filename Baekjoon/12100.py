import sys
from collections import deque
from  copy import deepcopy
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
                        break
        # print(board[i])
        for j in range(N-1):

            if board[i][j] == board[i][j+1]:
                board[i][j] *= 2
                board[i][j+1] = 0
        # print(board[i])
        for j in range(N-1):
            if board[i][j] == 0:
                for k in range(j+1,N):
                    if board[i][k] != 0:
                        board[i][j], board[i][k] = board[i][k], board[i][j]
                        break
        # print(board[i])
def right():
    for i in range(N):
        for j in range(N-1, 0, -1):
            if board[i][j] == 0:
                for k in range(j-1, -1, -1):
                    if board[i][k] != 0:
                        board[i][j], board[i][k] = board[i][k], board[i][j]
                        break

        for j in range(N-1, 0, -1):

            if board[i][j] == board[i][j-1]:
                board[i][j] *= 2
                board[i][j-1] = 0

        for j in range(N-1, 0, -1):
            if board[i][j] == 0:
                for k in range(j-1, -1, -1):
                    if board[i][k] != 0:
                        board[i][j], board[i][k] = board[i][k], board[i][j]
                        break

def up():
    for i in range(N): # x
        for j in range(N-1): # y
            if board[j][i] == 0:
                for k in range(j+1,N):
                    if board[k][i] != 0:
                        board[j][i], board[k][i] = board[k][i], board[j][i]
                        break
        for j in range(N-1):

            if board[j][i] == board[j+1][i]:
                board[j][i] *= 2
                board[j+1][i] = 0
        for j in range(N-1):
            if board[j][i] == 0:
                for k in range(j + 1, N):
                    if board[k][i] != 0:
                        board[j][i], board[k][i] = board[k][i], board[j][i]
                        break
def down():
    for i in range(N): # x
        for j in range(N-1, 0, -1): # y
            if board[j][i] == 0:
                for k in range(j-1, -1, -1):
                    if board[k][i] != 0:
                        board[j][i], board[k][i] = board[k][i], board[j][i]
                        break
        for j in range(N-1, 0, -1):

            if board[j][i] == board[j-1][i]:
                board[j][i] *= 2
                board[j-1][i] = 0
        for j in range(N-1, 0, -1):
            if board[j][i] == 0:
                for k in range(j-1, -1, -1):
                    if board[k][i] != 0:
                        board[j][i], board[k][i] = board[k][i], board[j][i]
                        break
# print(board)



def whichdir(x):
    if x == 1:
        up()
    elif x == 2:
        down()
    elif x == 3:
        right()
    else:
        left()
    # for i in range(N):
    #     print(board[i])
    # print("-------------------------------------------------------")
#
# whichdir(3)
# whichdir(1)
# whichdir(3)
# whichdir(1)
# whichdir(3)

cnt = 0
answer = 0
tmp = deepcopy(board)

#

for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            for d in range(1, 5):
                for e in range(1, 5):
                    board = deepcopy(tmp)

                    whichdir(a)
                    whichdir(b)
                    whichdir(c)
                    whichdir(d)
                    whichdir(e)


                    for x in range(N):
                        answer = max(answer, max(board[x]))


print(answer)


