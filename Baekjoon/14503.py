import sys
read = sys.stdin.readline
N, M = map(int ,read().split())
r, c, d = map(int, read().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, read().split())))

def find():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == -1:
                cnt+=1
    print(cnt)

def sol():
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    cy, cx, cd = r, c, d

    while True:
        maps[cy][cx] = -1 # 1번
        tmpd = cd - 1  # 2번
        if tmpd == -1:
            tmpd = 3
        ny = cy + dy[tmpd]
        nx = cx + dx[tmpd]
        if maps[ny][nx] == 0:
            cd = tmpd
            cy = ny
            cx = nx
            continue
        else:
            if maps[cy+dy[0]][cx+dx[0]] != 0 \
                    and maps[cy+dy[1]][cx+dx[1]] != 0 \
                    and maps[cy+dy[2]][cx+dx[2]] != 0 \
                    and maps[cy+dy[3]][cx+dx[3]] != 0:
                back = cd + 2
                if back == 4:
                    back = 0
                elif back == 5:
                    back = 1
                if maps[cy+dy[back]][cx+dx[back]] == 1:
                    return
                else:
                    cy += dy[back]
                    cx += dx[back]
            else:
                # c번
                cd = tmpd
                continue

sol()
find()