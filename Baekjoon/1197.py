import sys
read = sys.stdin.readline
def find(node):
    if parents[node] == node:
        return node
    parents[node] = find(parents[node])
    return parents[node]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def check(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    else:
        return False

V, E = map(int,read().split())
parents = [i for i in range(V+1)]
lines = list()
for _ in range(E):
    first, last, value = map(int, read().split())
    lines.append([first, last, value])
sorted_lines = sorted(lines, key=lambda x:x[2])

distance = 0
for line in sorted_lines:
    if not check(line[0], line[1]):
        union(line[0], line[1])
        distance += line[2]
print(distance)



