import sys
read = sys.stdin.readline
N, M, H = map(int, read().split())
ladder = [['0'] * (N+1) for _ in range(H+1)]
minValue = sys.maxsize
for _ in range(M):
    a, b = map(int, read().split())
    ladder[a][b] = '<'
    ladder[a][b+1] = '>'

def go():
    for j in range(1, N+1):
        currentPosition = j
        for i in range(1, H+1):
            if ladder[i][currentPosition] == '0':
                continue
            else:
                if ladder[i][currentPosition] == '>':
                    currentPosition -= 1
                elif ladder[i][currentPosition] == '<':
                    currentPosition += 1
        if currentPosition != j:
            return False
    return True

def findBridge(bridge, a=1):
    global minValue

    if bridge > 3 or bridge >= minValue :
        return

    for j in range(a, N):
        for i in range(1, H+1):
            if not(ladder[i][j] == '<' or ladder[i][j]=='>'or \
                    ladder[i][j-1] == '<'or\
                    ladder[i][j+1] == '<' or ladder[i][j+1]=='>'):
                ladder[i][j] = '<'
                ladder[i][j+1] = '>'

                Flag = go()
                if Flag:
                    minValue = min(minValue, bridge)

                else:
                    findBridge(bridge+1, j)
                ladder[i][j] = '0'
                ladder[i][j + 1] = '0'

def sol():
    if M == 0:
        print(0)
        return

    findBridge(ladder, 1)
    if minValue == sys.maxsize:
        print(-1)
    else:
        print(minValue)


sol()