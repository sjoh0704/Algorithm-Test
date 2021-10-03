import sys
read = sys.stdin.readline
N, M = map(int, read().split())
case = []
for _ in range(M):
    case.append(list(map(int ,read().split())))
print(case)
