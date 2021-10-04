import sys
read = sys.stdin.readline
N, M = map(int, read().split())

case = []
area = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int ,read().split())
    area[a][b] += 1
stack = []
for i in range(1, N+1):
    for j in range(1, N+1):
        if area[i][j] == 0:
            stack.append([i, j])
ans = set()
while stack:
    a, b = stack.pop()
    print(a, b)
    ans.add(a)
    for i in range(1, N+1):
        if area[b][i] > 0:
            area[b][i] -= 1
            if area[b][j] == 0:
                stack.append([b, i])


ans = list(ans)[::-1]
for a in ans:
    print(a, end=" ")




