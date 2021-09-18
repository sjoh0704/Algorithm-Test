import sys
from time import sleep
read = sys.stdin.readline
N, K = map(int, read().split())
color = []
for _ in range(N):
    color.append(list(map(int, read().split())))

area = [[[] for _ in range(N)] for _ in range(N)]

for i in range(1, K+1):
    y, x, d = map(int, read().split())
    area[y-1][x-1].append([i, d])

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]

def turn():
    for i in range(1, K+1):

        FLAG = False
        for j in range(N):
            for k in range(N):
                elem = area[j][k]
                for l in range(len(elem)):
                    if elem[l][0] == i:
                        cdir = elem[l][1]
                        FLAG = True
                        ny = dy[cdir] + j
                        nx = dx[cdir] + k
                        if not(0<=ny<N and 0<=nx<N) or color[ny][nx] == 2:
                      
                            if cdir == 1:
                                cdir = 2
                            elif cdir == 2:
                                cdir = 1
                            elif cdir == 3:
                                cdir = 4
                            elif cdir == 4:
                                cdir = 3
                            ny = dy[cdir] + j
                            nx = dx[cdir] + k
                            area[j][k][l][1] = cdir

                            if not(0<=ny<N and 0<=nx<N) or color[ny][nx] == 2:
                                area[j][k][l][1] = cdir
                            else:
                                if color[ny][nx] == 1:
                                    area[ny][nx].extend(elem[l:][::-1])
                                    area[j][k] = elem[:l]
                                elif color[ny][nx] == 0:
                                    area[ny][nx].extend(elem[l:])
                                    area[j][k] = elem[:l]
                                if len(area[ny][nx]) >= 4:
                                    return 1
                        else:
                            if color[ny][nx] == 1:
                                area[ny][nx].extend(elem[l:][::-1])
                                area[j][k] = elem[:l]
                            elif color[ny][nx] == 0:
                                area[ny][nx].extend(elem[l:])
                                area[j][k] = elem[:l]
                            if len(area[ny][nx]) >= 4:
                                return 1

                    if FLAG:    
                        break
                if FLAG:
                    break
            if FLAG:
                break
    return -1

cnt = 0
while 1:
    cnt += 1  
    check = turn()

    if check == 1:
        print(cnt)
        break
    elif cnt > 1000:
        print(-1)
        break
  
# for a in area:
#     print(a)                        
# print()