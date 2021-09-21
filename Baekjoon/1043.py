import sys
read = sys.stdin.readline
N, M = map(int ,read().split())
know = list(map(int ,read().split()))[1:]
partys = []
for _ in range(M):
    partys.append(list(map(int, read().split()))[1:])


black = []
for k in know:
    for party in partys:
        if k in party:
            black.extend(party)
black = list(set(black))

cnt = 0
for party in partys:
    for b in black:
        if b in party:
            cnt += 1
            break
   
ans = M - cnt
print(ans)