from collections import deque
n = int(input())
dir = ["L", "R", "U", "D"]
dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]
dir_set = deque(input().split())
y, x = 1, 1

while dir_set:
    d = dir_set.popleft()
    for i in range(len(dir)):
        if d == dir[i] and 1<=x+dxy[i][0]<=n and 1<=y+dxy[i][1]<=n:
             x += dxy[i][0]
             y += dxy[i][1]
print(x, y)