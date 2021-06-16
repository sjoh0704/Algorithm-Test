import sys
read = sys.stdin.readline
N = int(read().strip())
A = list(map(int ,read().split()))
B, C = map(int ,read().split())

cnt = N
for i in range(N):
    A[i] -= B
    if A[i] < 0:
        A[i] = 0

    while A[i] > 0:
        A[i] -= C
        cnt += 1
    else:
        A[i] = 0
print(cnt)