from copy import deepcopy
import sys
read = sys.stdin.readline
N, M = map(int, read().split())
area_main = []
cctv_loc = []
for i in range(N):
    tmp_area = list(map(int, read().split()))
    area_main.append(tmp_area)
    for j in range(M):
        if tmp_area[j] == 1 or tmp_area[j] == 2 or tmp_area[j] == 3 or tmp_area[j] == 4 or tmp_area[j] == 5:
            cctv_loc.append([tmp_area[j], i, j])
look = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [3, 0]], [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], [[0, 1, 2, 3]]]
cnt = 0
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
ans = sys.maxsize

def sol(cnt, area):
    if cnt == len(cctv_loc):
        global ans
        tmp = 0
        for i in range(N):
            for j in range(M):
                if area[i][j] == 0:
                    tmp += 1
        ans = min(ans, tmp)
    else:
        which_cctv, y, x = cctv_loc[cnt]
        for cctv_dir in look[which_cctv]:
            tmp = deepcopy(area)
            for cd in cctv_dir:
                dy, dx = dir[cd]
                tmp_y = y + dy
                tmp_x = x + dx
                while 0 <= tmp_y < N and 0 <= tmp_x < M and tmp[tmp_y][tmp_x] != 6:
                    tmp[tmp_y][tmp_x] = -1
                    tmp_y += dy
                    tmp_x += dx
            sol(cnt + 1, tmp)
sol(0, area_main)
print(ans)