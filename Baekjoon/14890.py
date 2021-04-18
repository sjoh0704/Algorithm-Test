import sys
read = sys.stdin.readline
def check(maps, cnt, N, L):
    for i in range(N):
        # 행에 대해서 실시
        end = -1  # 겹치는 경우 체크
        before = maps[i][0]
        Flag = True  # 경사로가 만들어졌는지 체크
        for j in range(1, N):
            if before < maps[i][j]: # 증가하는 경사로를 만드는 경우
                for k in range(1, L+1):
                    if not(j >= k and maps[i][j-k] == maps[i][j] -1 and end < j-k):
                        Flag = False
                        break
            elif before > maps[i][j]: # 감소하는 경사로를 만드는 경우
                for k in range(L):
                    if not(N > j + k and maps[i][j+k] == before - 1):
                        Flag = False
                        break
            else:  # 경사로가 필요없는 경우
                pass
                if Flag:
                    end = j + L -1
            before = maps[i][j]
        if Flag:
            cnt += 1

        # 열에 대해서 실시
        end = -1
        before = maps[0][i]
        Flag = True
        for j in range(1, N):
            if before < maps[j][i]:
                for k in range(1, L + 1):
                    if not (j >= k and maps[j - k][i] == maps[j][i] - 1 and end < j-k):
                        Flag = False
                        break
            elif before > maps[j][i]:
                for k in range(L):
                    if not (j+k < N and maps[j + k][i] == before - 1):
                        Flag = False
                        break
                if Flag:
                    end = j + L -1
            before = maps[j][i]
        if Flag:
            cnt += 1

    return cnt


def sol():
    N, L = map(int, read().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, read().split())))
    cnt = check(maps, 0, N, L)
    print(cnt)

sol()