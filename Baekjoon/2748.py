import sys
n = int(sys.stdin.readline())
if n < 2:
    print(n)
else:
    fivo = [0 for _ in range(n+1)]
    fivo[1], fivo[2] = 1, 1
    for i in range(3, n+1):
        fivo[i] = fivo[i-1] + fivo[i-2]
    print(fivo[n])