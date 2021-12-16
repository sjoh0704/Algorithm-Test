import sys
read = sys.stdin.readline
N = int(read())
tmp = []
for _ in range(N):
    tmp.append(int(read()))
tmp.sort()
for t in tmp:
    print(t)