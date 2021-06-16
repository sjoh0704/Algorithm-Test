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
    cnt += (A[i] // C)
    if A[i] % C != 0:
        cnt += 1
print(cnt)