import sys
from collections import deque
read =sys.stdin.readline
R, C, M = map(int, read().split())
area = [[[] for _ in range(C+1)] for _ in range(R+1)]
for _ in range(M):
    r, c, s, d, z = map(int, read().split())
    area[r][c].append([s, d, z]) 
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]
def move():
    result = [[[] for _ in range(C+1)] for _ in range(R+1)]
    for i in range(1, C+1):
        for j in range(1, R+1):
            if len(area[j][i]) != 0:
                cs = area[j][i][0]
                speed = cs[0]
                dir = cs[1]
                size = cs[2]
                cy, cx = j, i
                while speed:
                    cx += dx[dir]
                    cy += dy[dir]
                    if cx == 0:
                        cx = 2
                        dir = 3
                    elif cx == C + 1:
                        cx = C - 1  
                        dir = 4
                    elif cy == 0:
                        cy = 2
                        dir = 2
                    elif cy == R + 1:
                        cy = R-1
                        dir = 1
                    speed -= 1
                result[cy][cx].append([cs[0], dir, cs[2]])
                if len(result[cy][cx]) > 0:
                    if result[cy][cx][0][2] < size:
                        result[cy][cx][0] = [cs[0], dir, size]  
                else:
                     result[cy][cx].append([cs[0], dir, size])
    return result
totalSize= 0
for i in range(1, C+1):
    for j in range(1, R+1):
        if len(area[j][i]) != 0:
            totalSize += area[j][i][0][2]
            area[j][i] = []
            break
    area = move()
print(totalSize)
