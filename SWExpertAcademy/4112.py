from collections import deque
read = input
T = int(read().strip())

def find(x):
    returny, returnx = 0, 0
    for i in range(1, x+1):
        x -= i
        if x <= 0:
            returny = i - 1
            returnx = x + i - 1
            break
    return [returny, returnx]

def sol():
    a, b = map(int, read().split())
    high = max(a, b)
    pyramid = []

    start = find(a)
    end = find(b)
    if start == end:

        return 0

    for i in range(1, high):
        # pyramid.append([0 for _ in range(i)])
        high -= i
        if high < 0:
            pyramid = [[0 for _ in range(i)] for _ in range(i)]
            break
    for i in range(len(pyramid)):
        for j in range(len(pyramid)):
            if j < i:
                pyramid[j][i] = -1


    dxy = [[1, 1],[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1]]
    queue = deque([start])
    count = deque([0])
    while queue:
        cy, cx = queue.popleft()
        cc = count.popleft()
        if pyramid[cy][cx] == 0:
            pyramid[cy][cx] = 1
            if cy == end[0] and cx == end[1]:

                return cc
            for i in range(len(dxy)):
                tmpy =cy + dxy[i][0]
                tmpx =cx + dxy[i][1]
                if 0<= tmpy < len(pyramid) and 0 <= tmpx < len(pyramid) and pyramid[tmpy][tmpx] != -1:
                    queue.append([tmpy, tmpx])
                    count.append(cc+1)
answer = []
for i in range(T):
    answer.append(sol())
for i in range(T):
    print("#{} {}".format(i+1, answer[i]))

