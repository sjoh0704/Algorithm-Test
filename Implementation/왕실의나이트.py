start = input()
let, x = start[0], int(start[1])
col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
y = col.index(let) + 1
dx = [[2, 1], [-2, -1], [-2, 1], [2, -1], [1, 2],
       [-1, -2],[-1, 2],[1, -2]]
cnt = 0
for d in dx:
    dy = y + d[1]
    dx = x + d[0]
    if 1 <= dx <= 8 and 1 <= dy <= 8:
       cnt += 1
print(cnt)
