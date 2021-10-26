from collections import deque
import sys
read = sys.stdin.readline
N = int(read())
M = int(read())
dic = {}
for i in range(1, M+1):
    tmp = list(map(int ,read().split()))
    for j in range(1, N+1):
        if tmp[j-1]: 
            if i not in dic:
                dic[i] = [j]
            else:
                dic[i].append(j)

# print(dic)
move = deque(list(map(int, read().split())))
# print(move)



def dfs(start):
    stack = [start]

    while move and stack:
        cs = stack.pop()
        # print(cs)
        if move[0] == cs:
            x = move.popleft()
            # print(x)
        for ns in dic[cs]:
            stack.append(ns)
    
    if move:
        print("FALSE")
    else:
        print("YES")

dfs(move[0])

