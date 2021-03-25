import sys
from collections import deque
read = sys.stdin.readline
status = []
for _ in range(4):
    status.append(deque(map(int, list(read().strip()))))
relationship = {1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}
K = int(read())
turn = []
for _ in range(K):
    turn.append(list(map(int , read().split())))
def dfs(which, dir):
    visit = [0 for _ in range(4)]
    cs = []
    for i in range(4):
        cs.append([status[i][6], status[i][2]])
    stack = [[which, dir]]
    while stack:
        cw, cd = stack.pop()
        tmp = cd
        if visit[cw-1]:
            continue
        visit[cw-1] = 1
        if cd == 1:
            status[cw-1].appendleft(status[cw-1].pop())
        elif cd == -1:
            status[cw-1].append(status[cw-1].popleft())
        for x in relationship[cw]:
            cd = tmp
            if (cs[x-1][1] != cs[cw-1][0] and x<cw) or (cs[x-1][0] != cs[cw-1][1] and x >= cw):
                if cd == 1:
                    cd = -1
                elif cd == -1:
                    cd = 1
                else:
                    cd = 0
            else:
                cd = 0
            stack.append([x, cd])
for which, dir in turn:
    dfs(which, dir)
sum = 0
for i in range(4):
    if status[i][0] == 1:
        sum += 2**i
print(sum)