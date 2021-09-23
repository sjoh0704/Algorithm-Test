from collections import deque
import sys
from itertools import combinations
read = sys.stdin.readline
tmp = read().split()
N = tmp[0]
K = int(tmp[1])
pairs = list(combinations(list(range(1, len(N)+1)), 2))

def swap_number(n, pair):
    n_list = list(n)    
    a, b = map(lambda x:x-1, pair)
    tmp = n_list[a]
    n_list[a] = n_list[b]
    n_list[b] = tmp
    return "".join(n_list)

total = set()
visited = [[False for _ in range(10000001)] for _ in range(K+1)]
def bfs():
    queue = deque()
    queue.append([N, 0])
    ret = 0
    while queue:
        cn, cc = queue.popleft()

        if cc == K:
            ret = max(ret, int(cn))
            continue
        if visited[cc][int(cn)]:
            continue
            visit[cc][int(cn)] = True

        for pair in pairs:
            nn = swap_number(cn, pair)
            if nn[0] == "0":
                continue
            queue.append([nn, cc + 1])
    return ret
ans = bfs()
if not ans:
    print(-1)
else:
    print(ans)      


