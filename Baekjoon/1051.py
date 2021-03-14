import sys
read = sys.stdin.readline
N, M = map(int, read().split())
square = []
for _ in range(N):
    square.append(list(map(int, list(read().strip()))))


def find_sqaure(y, x):
    num = square[y][x]
    global ans
    i = 0
    while 0 <= y+i < N and 0 <= x+i < M:
        if square[y+i][x] == square[y][x+i] == square[y+i][x+i] == num:
            ans = max(ans, (i+1)**2)
        i += 1


ans = 0
for y in range(N):
    for x in range(M):
        find_sqaure(y, x)
print(ans)
