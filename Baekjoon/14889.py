import sys
from itertools import combinations, permutations
read = sys.stdin.readline
N = int(read())
status = []
for _ in range(N):
    status.append(list(map(int, read().split())))
comb = list(combinations(list(range(1, N+1)), N//2))

def solve(team):
    team1 = 0
    team2 = 0
    tmp1 = list(combinations(team, 2))

    for a, b in tmp1:
        team1 += status[a-1][b-1] + status[b-1][a-1]
    rest = []
    for i in range(1, N+1):
        if i not in team:
            rest.append(i)
    tmp2 = list(combinations(rest, 2))
    for a, b in tmp2:
        team2 += status[a-1][b-1] + status[b-1][a-1]
    return abs(team1-team2)

answer = 100000000000
for c in comb:
    tmp = solve(c)
    if answer > tmp:
        answer = tmp

print(answer)

    