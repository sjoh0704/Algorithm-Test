import sys
from collections import deque
read = sys.stdin.readline
case = int(read())


def sol():
    N, M = map(int, read().split())
    tmp = list(map(int, read().split()))
    queue = deque([(i, tmp[i])for i in range(N)])

    cnt = 0
    while queue:
        cur = queue.popleft()
        tmp = 0
        for q in queue:
            if cur[1] < q[1]:
                queue.append(cur)
                tmp = 1
                break
        if tmp == 0:
            cnt += 1
            if cur[0] == M:
                return cnt
    return -1

ans_list = []
for _ in range(case):
    ans_list.append(sol())

for a in ans_list:
    print(a)
