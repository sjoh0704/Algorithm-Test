import sys
from itertools import combinations
from collections import deque
read = sys.stdin.readline
N, K = map(int, read().split())
combi = list(combinations(range(1, len(str(N))+1), 2))
def swap(N, a, b):
    _N = list(N)
    _N[a-1], _N[b-1] = _N[b-1], _N[a-1]
    return "".join(_N)
def bfs(N, K):
    ans, cnt = 0, 0
    visit = []
    queue = deque([[N, cnt]])
    while queue:
        cq, cc = queue.popleft()
        if [cq, cc] in visit:
            continue
        visit.append([cq, cc])
        if cc == K:
            ans = max(ans, int(cq))
        for f, s in combi:
            next = swap(cq, f, s)
            if next[0] == "0" or cc + 1 > K:
                continue
            queue.append([next, cc+1])
    if ans == 0:
        print(-1)
    else:
        print(ans)
bfs(str(N), K)