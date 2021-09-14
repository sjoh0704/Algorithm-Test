import sys
read = sys.stdin.readline
N, K = map(int ,read().split())
area = []
for _ in range(N):
    area.append(list(map(int, read().split())))
horses = []
for _ in range(K):
    y, x, d  = map(int ,read().split())
    horses.append([y-1, x-1, d-1])
 
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

state = [[[]for _ in range(N)]for _ in range(N)]
for i, h in enumerate(horses):
    state[h[0]][h[1]].append([i, h[2]])

def sol():
    for i in range(K):
        FLAG = True
        for j in range(N):
            for k in range(N):
                for l, s in enumerate(state[j][k]):
                    if s[0] == i:
                        FLAG = False
                        cd = s[1]        
                        ny = j + dy[cd]
                        nx = k + dx[cd]
                        if not(0<=ny<N and 0<=nx<N) or area[ny][nx] == 2:
                            nd = 1 if cd == 0 else ( \
                            0 if cd == 1 else (\
                            2 if cd == 3 else (\
                            3 if cd == 2 else -1)))       
                            ny = j + dy[nd]
                            nx = k + dx[nd]
                            if  not(0<=ny<N and 0<=nx<N) or area[ny][nx] == 2:
                                state[j][k][l][1] = nd   
                            else:

                                if area[ny][nx] == 0:
                                    state[ny][nx].extend(state[j][k][l:])
                                    state[j][k] = state[j][k][:l]
                                elif area[ny][nx] == 1:
                                    state[ny][nx].extend(state[j][k][l:][::-1])
                                    state[j][k] = state[j][k][:l]
                                if len(state[ny][nx]) == K:
                 
                                    return 1

                        else:
                            if area[ny][nx] == 0:
                                state[ny][nx].extend(state[j][k][l:])
                                state[j][k] = state[j][k][:l]
                            elif area[ny][nx] == 1:
                                state[ny][nx].extend(state[j][k][l:][::-1])
                                state[j][k] = state[j][k][:l]
                            print(state[ny][nx])
                            if len(state[ny][nx]) == K:
                                return 1
                        break
                    
                if not FLAG:
                    break

            if not FLAG:
                break
    return -1
cnt = 0
while True:
    cnt += 1
    check = sol()
    if check == 1:
        print(cnt)
        break 
    if cnt > 1000:
        print(-1)
        break

    

# for s in state:
#     print(s)






