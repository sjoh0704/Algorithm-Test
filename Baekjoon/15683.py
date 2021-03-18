import sys
from copy import deepcopy
read = sys.stdin.readline


cctv = (1, 2, 3, 4, 5)
N, M = map(int, read().split())
area = []
target = []
cctv_cnt = 0
for i in range(N):
    tmp = list(map(int, read().split()))
    area.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] in cctv:
            target.append((i, j))

def check(area, dir, y, x):
    print("fini", area)
    print("aaa",area[y])
    print("bbb",area[y][x])
    num = area[y][x]
    if num == 1:
        if dir == 1:
            for i in range(y-1, -1, -1):
                if area[i][x] != 6:
                    if not area[i][x] in cctv:
                        area[i][x] = -1
                else:
                    break
        elif dir == 2:
            for i in range(x+1, M):
                if area[y][i] != 6:
                    if not area[y][i] in cctv:

                        area[y][i] = -1
                else:
                    break
        elif dir == 3:
            for i in range(y+1, N):
                if area[i][x] != 6:
                    if not area[i][x] in cctv:
                        area[i][x] = -1

                else:
                    break
        elif dir == 4:
            for i in range(x-1, -1, -1):
                if area[y][i] != 6:
                    if not area[y][i] in cctv:
                        area[y][i] = -1

                else:
                    break
    if num == 2:
        if dir == 1 or dir ==3:
            for i in range(y-1, -1, -1):
                if area[i][x] != 6:
                    if not area[i][x] in cctv:
                        area[i][x] = -1
                else:
                    break
            for i in range(y+1, N):
                if area[i][x] != 6:
                    if not area[i][x] in cctv:
                        area[i][x] = -1
                else:
                    break
        elif dir == 2 or dir ==4:
            for i in range(x+1, M):
                if area[y][i] != 6:
                    if not area[y][i] in cctv:
                        area[y][i] = -1
                else:
                    break
            for i in range(x-1, -1, -1):
                if area[y][i] != 6:
                    if not area[y][i] in cctv:
                        area[y][i] = -1
                else:
                    break


    if num == 3:
        if dir == 1:
            for i in range(y-1, -1, -1):
                if area[i][x] != 6:
                    if not area[i][x] in cctv:
                        area[i][x] = -1
                else:
                    break
            for i in range(x+1, M):
                if area[y][i] != 6:
                    if not area[y][i] in cctv:
                        area[y][i] = -1
                else:
                    break

        elif dir == 2:
            for i in range(x+1, M):
                if area[y][i] != 6:
                    if not area[y][i] in cctv:
                        area[y][i] = -1
                else:
                    break
            for i in range(y+1, N):
                if area[i][x] != 6:
                    if not area[i][x] in cctv:
                        area[i][x] = -1
                else:
                    break


        elif dir == 3:
            for i in range(y+1, N):
                if area[i][x] != 6:
                    if not area[i][x] in cctv:
                        area[i][x] = -1
                else:
                    break
            for i in range(x-1, -1, -1):
                if area[y][i] != 6:
                    if not area[y][i] in cctv:
                        area[y][i] = -1
                else:
                    break

        elif dir == 4:
            for i in range(x-1, -1, -1):
                if area[y][i] != 6:
                    if not area[y][i] in cctv:
                        area[y][i] = -1
                else:
                    break
            for i in range(y-1, -1, -1):
                if area[i][x] != 6:
                    if not area[i][x] in cctv:
                        area[i][x] = -1
                else:
                    break
    if num == 4:
        if dir == 1:
            for i in range(y - 1, -1, -1):
                if area[i][x] != 6:
                    if not area[i][x] in cctv:
                        area[i][x] = -1
                else:
                    break
            for i in range(x + 1, M):
                if area[y][i] != 6:
                    if not area[y][i] in cctv:
                        area[y][i] = -1
                else:
                    break
            for i in range(y + 1, N):
                if area[i][x] != 6:
                    if not area[i][x] in cctv:
                        area[i][x] = -1
                else:
                    break

        elif dir == 2:
            for i in range(x + 1, M):
                if area[y][i] != 6:
                    if not area[y][i] in cctv:
                        area[y][i] = -1
                else:
                    break
            for i in range(y + 1, N):
                if area[i][x] != 6:
                    if not area[i][x] in cctv:
                        area[i][x] = -1
                else:
                    break
            for i in range(x - 1, -1, -1):
                if area[y][i] != 6:
                    if not area[y][i] in cctv:
                        area[y][i] = -1
                else:
                    break


        elif dir == 3:
            for i in range(y + 1, N):
                if area[i][x] != 6:
                    if not area[i][x] in cctv:
                        area[i][x] = -1
                else:
                    break
            for i in range(x - 1, -1, -1):
                if area[y][i] != 6:
                    if not area[y][i] in cctv:
                        area[y][i] = -1
                else:
                    break
            for i in range(y - 1, -1, -1):
                if area[i][x] != 6:
                    if not area[i][x] in cctv:
                        area[i][x] = -1
                else:
                    break

        elif dir == 4:
            for i in range(x - 1, -1, -1):
                if area[y][i] != 6:
                    if not area[y][i] in cctv:
                        area[y][i] = -1
                else:
                    break
            for i in range(y - 1, -1, -1):
                if area[i][x] != 6:
                    if not area[i][x] in cctv:
                        area[i][x] = -1
                else:
                    break
            for i in range(y + 1, N):
                if area[i][x] != 6:
                    if not area[i][x] in cctv:
                        area[i][x] = -1
                else:
                    break
    if num == 5:
        if dir == 1 or dir == 2 or dir==3 or dir ==4:
            for i in range(y-1, -1, -1):
                if area[i][x] != 6:
                    if not area[i][x] in cctv:
                        area[i][x] = -1
                else:
                    break

            for i in range(x+1, M):
                if area[y][i] != 6:
                    if not area[y][i] in cctv:
                        area[y][i] = -1
                else:
                    break

            for i in range(y+1, N):
                if area[i][x] != 6:
                    if not area[i][x] in cctv:
                        area[i][x] = -1
                else:
                    break

            for i in range(x-1, -1, -1):
                if area[y][i] != 6:
                    if not area[y][i] in cctv:
                        area[y][i] = -1
                else:
                    break

cp_area = deepcopy(area)
cnt = 0
ordered_list = [0 for _ in range(len(target))]
def make_order(cnt):

    if cnt == len(target):

        area = deepcopy(cp_area)
        print(area)

        for i in range(len(target)):

            y, x = target[i]
            # print(target[i])

            check(area, ordered_list[i], y, x)
            # for i in range(N):
            #     print(area[i])

    else:
        for i in range(1, 5):

            ordered_list[cnt] = i
            cnt += 1
            make_order(cnt)
            cnt -= 1

make_order(cnt)

check(area[1][1], 2, 1,1)
print(area)

#
# for i in range(N):
#     for j in range(M):
#         check(area[i][j], 1, i, j)
#
# print(area)




