import sys
read =sys.stdin.readline
R, C, M = map(int, read().split())
area = [[[]] * (C+1) for _ in range(R+1)]
for _ in range(M):
    r, c, s, d, z = map(int, read().split())
    area[r][c] = [s, d, z]

for a in area:
    print(a)

totalSize= 0
for i in range(1, C+1):
    for j in range(1, R+1):
        if len(area[j][i]) != 0:
            totalSize += area[j][i][2]
            area[j][i] = []
            break
print(totalSize)


def move():
    for i in range(1, C+1):
        for j in range(1, R+1):
            if len(area[j][i]) != 0:
                dir = area[j][i][1]
                speed = area[j][i][0]
                if dir == 1:
                    _col = 0
                    if j-speed > 0:
                        _col = j - speed
                    else:
                        



for a in area:
    print(a)