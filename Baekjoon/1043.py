from collections import deque
import sys
read = sys.stdin.readline
N, M = map(int ,read().split())
know = deque(list(map(int ,read().split()))[1:])
partys = []
for _ in range(M):
    partys.append(list(map(int, read().split()))[1:])
visit = [False] * (N+1)
check = [True] * M
while know:
    ck = know.pop()
    if visit[ck]:
        continue
    visit[ck] = True
    for i, party in enumerate(partys):
        if ck not in party:
            continue
        check[i] = False
        for p in party:
            if p != ck:  
                know.append(p)            
cnt = 0
for c in check:
    if c:
        cnt += 1
print(cnt)