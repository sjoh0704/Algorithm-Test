import sys
read = sys.stdin.readline
N, M, H = map(int, read().split())
ladder = [['0'] * (N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, read().split())
    ladder[a][b] = '<'
    ladder[a][b+1] = '>'
answer = -1
minValue = sys.maxsize

def go(start):
    currentPosition = start
    for i in range(1, H+1):
        if ladder[i][currentPosition] == '0':
            continue
        else:
            if ladder[i][currentPosition] == '>':
                currentPosition -= 1
            elif ladder[i][currentPosition] == '<':
                currentPosition += 1

    if currentPosition == start:
        return True
    else:
        return False

def findBridge(ladder, bridge):
    global minValue
    global answer
    # print("findBridge")
    if bridge > 3:
        return

    for j in range(1, N):
        for i in range(1, H+1):
            if ladder[i][j] == '<' or ladder[i][j]=='>'or \
                    ladder[i][j-1] == '<'or\
                    ladder[i][j+1] == '<' or ladder[i][j+1]=='>':
                continue

            else:
                ladder[i][j] = '<'
                ladder[i][j+1] = '>'
                Flag = True
                for k in range(1, N+1):
                    if not go(k):
                        Flag = False
                        break
                if Flag:
                    minValue = min(minValue, bridge)

                else:
                    findBridge(ladder, bridge+1)

                ladder[i][j] = '0'
                ladder[i][j + 1] = '0'

def sol(ladder):
    if M == 0:
        print(0)
        return

    findBridge(ladder, 1)
    if minValue == sys.maxsize:
        print(-1)
    else:
        print(minValue)


sol(ladder)