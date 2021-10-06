import sys
read = sys.stdin.readline
N = int(read())
M = int(read())
case = []
for _ in range(M):
    case.append(list(map(int ,read().split())))
sorted_case = sorted(case, key=lambda x:x[2]) 
parents = [i for i in range(N+1)]
def find(x):
    if parents[x] == x:
        return x            
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parents[x] = y
    elif x < y:
        parents[y] = x

def same_parents(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return True
    return False

ans = 0
for a, b, v in sorted_case:
    if not same_parents(a, b):
        union(a, b)
        ans += v
print(ans)

