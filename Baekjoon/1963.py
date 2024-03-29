from math import sqrt
import sys
from collections import deque
read = sys.stdin.readline
T = int(read())
case = []
for _ in range(T):
    case.append(list(map(int, read().split())))
def replace_num(num, idx, num_to_replace):
    tmp = list(map(int, list(str(num))))
    tmp[idx] = num_to_replace
    return int("".join(map(str, tmp)))
def check(num):
    cnt = 0
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True
def sol(num, target):
    visited = [0 for _ in range(10000)]
    queue = deque([[num, 0]])
    ans = int(1e9)
    while queue:
        cq, cc = queue.popleft()
        if visited[cq]:
            continue
        visited[cq] = 1
        if target == cq:
            ans = min(ans, cc)
        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0: 
                    continue
                nq = replace_num(cq, i, j)
                if check(nq):
                    queue.append([nq, cc+1])
    if ans == int(1e9):
        print("Impossible")
    else:
        print(ans)
for f, s in case:
    sol(f, s)