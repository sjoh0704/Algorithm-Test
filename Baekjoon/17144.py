import sys
read = sys.stdin.readline
R, C, T = map(int, read().split())
area = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cleaning = []
for i in range(R):
    tmp = list(map(int, read().split()))
    for j in range(len(tmp)):
        if tmp[j] == -1:
            cleaning.append([i, j])
    area.append(tmp)


def findDust():
    dust = []
    for i in range(R):
        for j in range(C):
            if area[i][j] != 0 and area[i][j] != -1:
                dust.append([i, j, area[i][j]])
    return dust
def spread(dust):
    for cy, cx, d in dust:
        tmp = 0

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0<= nx < C and 0<= ny <R and area[ny][nx] != -1:
                tmp += 1
                area[ny][nx] += (d // 5)
        area[cy][cx] -= tmp*(d//5)

def circulate_up(cy, cx):
    for i in range(cy-1, 0, -1):
        area[i][cx] = area[i-1][cx]
    for i in range(0, C-1):
        area[0][i] = area[0][i+1]
    for i in range(0, cy):
        area[i][C-1] = area[i+1][C-1]
    for i in range(C-1, 1, -1):
        area[cy][i] = area[cy][i-1]
    area[cy][cx+1] = 0

def circulate_down(cy, cx):
    for i in range(cy+1, R-1):
        area[i][0] = area[i+1][0]
    for i in range(0, C-1):
        area[R-1][i] = area[R-1][i+1]
    for i in range(R-1, cy, -1):
        area[i][C-1] = area[i-1][C-1]
    for i in range(C-1, 1, -1):
        area[cy][i] = area[cy][i-1]
    area[cy][cx+1] = 0


def result():
    sum = 0
    for i in range(R):
        for j in range(C):
            if area[i][j] != 0 and area[i][j] != -1:
                sum += area[i][j]
    print(sum)


for _ in range(T):
    spread(findDust())
    circulate_up(cleaning[0][0], cleaning[0][1])
    circulate_down(cleaning[1][0], cleaning[1][1])

result()



