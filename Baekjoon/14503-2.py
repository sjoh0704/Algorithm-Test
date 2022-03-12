import sys
read = sys.stdin.readline
N, M = map(int, read().split())
r, c, d = map(int, read().split())
area = []
ans = 0 

dx = [0, 1, 0, -1]  # 북0 동1 남2 서3
dy = [-1, 0, 1, 0]
for _ in range(N):
    area.append(list(map(int, read().split())))

def find_left(origin_dir):
    if origin_dir == 0:
        left_dir = 3
    elif origin_dir == 1:
        left_dir = 0
    elif origin_dir == 2:
        left_dir = 1
    else:
        left_dir = 2
    return left_dir

def find_back(origin_dir):
    if origin_dir == 0:
        left_dir = 2
    elif origin_dir == 1:
        left_dir = 3
    elif origin_dir == 2:
        left_dir = 0
    else:
        left_dir = 1
    return left_dir

# 청소 = -1
def clean():  
    global r, c, d, ans
    origin_dir = d
    if not area[r][c]:
        ans += 1
        area[r][c] = -1
    
    # 2
    left = find_left(d) # 왼쪽 찾기
    ny, nx = r + dy[left], c + dx[left]
    if area[ny][nx] != 1 and not area[ny][nx]: # a-청소할 공간 있음
        # 방향 전환 + 이동
        d = left
        r, c = ny, nx
        return False
    else:

        # c
        FLAG = True
        for i in range(4):
            if not area[dy[i]+r][dx[i]+c]:
                FLAG = False
                break
                
        if FLAG: # 네면 갈곳 없음
            back = find_back(origin_dir)
            nr, nc = r+dy[back],c+dx[back]
            
            # d
            if 0<=nr<N and 0<=nc<M and area[nr][nc] == 1: # 후진도 못하는 상황
                return True # 끝
            else: # 후진 가능
                r, c = nr, nc
        else:
            # b
            d = left      
    return False

end = clean()
while not end:
    end = clean()

print(ans)

    









