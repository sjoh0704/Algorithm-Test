from itertools import combinations
from collections import deque
import sys
from copy import deepcopy
read = sys.stdin.readline
N, M, D = map(int, read().split())
area = []
for _ in range(N):
    area.append(list(map(int, read().split())))
archer = list(combinations([i for i in  range(M)], 3))
def attack(archer, area):
    global target
    queue = deque(archer)
    
    while queue:
        FLAG = False
        cq = queue.popleft()
        for i in range(N-1, -1, -1):
            for j in range(M):
                if area[i][j] and abs(cq-j) + abs(N-i) <= D:
                    area[i][j] = 0
                    FLAG = True
                    target += 1
                    break
            if FLAG:
               break 

def down(area):
    end_check = 0
    for i in range(N-2, -1, -1):
        for j in range(M):
            area[i+1][j] = area[i][j]
            if not area[i][j]:
                end_check += 1
    for i in range(M):
        area[0][i] = 0
    if end_check == M*(N-1):
        return True

    return False

ans = 0
for a in archer:
    target = 0  
    tmp = deepcopy(area)
    end = False
    while not end:    
        attack(a, tmp)
        end = down(tmp)
    ans = max(ans, target)
print(ans)