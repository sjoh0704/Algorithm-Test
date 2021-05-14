import sys
from collections import deque
read = sys.stdin.readline
field = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for _ in range(12):
    field.append(list(read().strip()))


def bfs():
    visited = [[0, 0]]
    queue = deque()
    queue.append([0, 0])
    R = []
    G = []
    B = []
    P = []
    Y = []
    while queue:
        # for i in range(12):
        #     print(field[i])
        # print()
        cy, cx = queue.popleft()
        # print(cx, cy, field[cy][cx])
        # print(R)

        color = field[cy][cx]
        if color == 'R':
            if [cy, cx] in R:
                continue
            R.append([cy, cx])
            emptySide = True
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if 0 <= nx < 6 and 0 <= ny < 12 and field[ny][nx] == 'R':
                    if [ny, nx] not in R:
                        emptySide = False
                        visited.append([ny, nx])
                        queue.append([ny, nx])

            if emptySide:
                if len(R) >= 4:
                    for ry, rx in R:
                        field[ry][rx] = '.'
                R = []

        elif color == 'G':

            if [cy, cx] in G:
                continue
            G.append([cy, cx])
            emptySide = True
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if 0<= nx < 6 and 0<=ny<12 and field[ny][nx] == 'G':
                    if [ny, nx] not in G:
                        emptySide = False
                        visited.append([ny, nx])
                        queue.append([ny, nx])

            if emptySide:
                if len(G) >= 4:
                    for ry, rx in G:
                        field[ry][rx] = '.'
                G = []


        elif color == 'B':

            if [cy, cx] in B:
                continue

            B.append([cy, cx])

            emptySide = True

            for i in range(4):

                nx = cx + dx[i]

                ny = cy + dy[i]

                if 0 <= nx < 6 and 0 <= ny < 12 and field[ny][nx] == 'B':

                    if [ny, nx] not in B:
                        emptySide = False

                        visited.append([ny, nx])

                        queue.append([ny, nx])

            if emptySide:

                if len(B) >= 4:

                    for ry, rx in B:
                        field[ry][rx] = '.'

                B = []


        elif color == 'P':

            if [cy, cx] in P:
                continue

            P.append([cy, cx])

            emptySide = True

            for i in range(4):

                nx = cx + dx[i]

                ny = cy + dy[i]

                if 0 <= nx < 6 and 0 <= ny < 12 and field[ny][nx] == 'P':

                    if [ny, nx] not in P:
                        emptySide = False

                        visited.append([ny, nx])

                        queue.append([ny, nx])

            if emptySide:

                if len(P) >= 4:

                    for ry, rx in P:
                        field[ry][rx] = '.'

                P = []


        elif color == 'Y':

            if [cy, cx] in Y:
                continue
            Y.append([cy, cx])
            emptySide = True
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 <= nx < 6 and 0 <= ny < 12 and field[ny][nx] == 'Y':
                    if [ny, nx] not in Y:
                        emptySide = False
                        visited.append([ny, nx])
                        queue.append([ny, nx])
            if emptySide:
                if len(Y) >= 4:
                    for ry, rx in Y:
                        field[ry][rx] = '.'

                Y = []


        else:
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0<= nx < 6 and 0<=ny<12  and [ny, nx] not in visited :

                    visited.append([ny, nx])
                    queue.append([ny, nx])


def down():
    for i in range(6):
        tmp = 0
        for j in range(11, -1, -1):
            if field[j][i] != ".":
                for k in range(11, j, -1):
                    if field[k][i] == ".":
                        field[k][i] = field[j][i]
                        field[j][i] = '.'
                        break

def check(tmp, field):
    for i in range(12):
        for j in range(6):
            if field[i][j] != tmp[i][j]:
                return True
    return False

recursion = True
cnt = 0
while recursion:
    tmp = [item[:] for item in field]


    bfs()
    print("explosion")
    for i in range(12):
        print(field[i])
    print()
    cnt += 1
    down()
    print("down")
    for i in range(12):
        print(field[i])
    print()

    recursion = check(tmp, field)
    if not recursion:
        cnt -= 1

print(cnt)



#
# bfs(find())
# for i in range(12):
#     print(field[i])