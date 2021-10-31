import sys
read = sys.stdin.readline
N = int(read())
M = int(read())
parents = [i for i in range(N+1)]
area = []
for i in range(1, N+1):
    tmp = list(map(int ,read().split()))
    area.append(tmp)
move = list(map(int, read().split()))

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]
    
def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

def same_parents(x, y):
    x = find(x)
    y = find(y)
    if x==y:
        return True
    else:
        return False

for i in range(N):
    for j in range(N):
        if area[i][j]:
            union(i+1, j+1)

FLAG = True
for i in range(M-1):
    if not same_parents(move[i], move[i+1]):
        FLAG = False
        break
if FLAG:
    print("YES")
else:
    print("FALSE")
