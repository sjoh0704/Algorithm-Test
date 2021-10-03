import sys
read = sys.stdin.readline
N, M = map(int, read().split())
case = []
for _ in range(M):
    case.append(list(map(int ,read().split())))
cnt = [0] * (N+1)
stack = []
for c1, c2 in case:
    cnt[c2] += 1
for i in range(1, N+1):
    if cnt[i] == 0:
        stack.append(i)
        cnt[i] = 'x'
ans = []
while stack:
    cp = stack.pop()
    ans.append(cp)
    for c1, c2 in case:
        if c1 == cp:
            cnt[c2] -= 1
    for i in range(1, N+1):
        if cnt[i] == 0:
            stack.append(i)
            cnt[i]='x'
    
for a in ans:
    print(a, end=' ')
print()


