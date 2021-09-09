import sys
read = sys.stdin.readline
N = int(read())
area = []
for _ in range(N):
    area.append(list(map(int ,read().split())))


def sol(y, x, d1, d2):
    if not(0<= y and y + d1+d2 < N and 0<= x-d1 and x+d2 < N):
        return 10000000
    edges = [[y, x], [y+d1, x-d1], [y+d2, x+d2], [y+d1+d2, x-d1+d2]]
    left, right = edges[0][1], edges[0][1]
    div = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(edges[0][0], edges[3][0]+1):
        for j in range(left, right+1):
            div[i][j] = 5
        if i >= edges[1][0]:
            left += 1
        else:
            left -= 1
        if i >= edges[2][0]:
            right -= 1
        else:
            right += 1
    population = [0 for _ in range(6)]
    for i in range(N):
        for j in range(N):
            if div[i][j] == 0:
                if j <= edges[0][1] and i < edges[1][0]:
                    population[1] += area[i][j]
                elif j > edges[0][1] and i <= edges[2][0]:
                    population[2] += area[i][j]
                elif j < edges[3][1] and i >= edges[1][0]:
                    population[3] += area[i][j]
                elif j >= edges[3][1] and i > edges[2][0]:
                    population[4] += area[i][j]
            else:
                population[5] += area[i][j]
    return max(population) - min(population[1:])

ans = 10000000
for a in range(N):
    for b in range(N):
        for c in range(1, N):
            for d in range(1, N):
                ans = min(ans, sol(a, b, c, d))
print(ans)
