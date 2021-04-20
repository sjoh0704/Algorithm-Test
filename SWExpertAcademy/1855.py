from collections import deque
T = int(input())
def dfs(graph, current, next):
    cnt = 0
    stack = [[current, cnt]]
    visited = [current]
    while stack:


        cn, cc = stack.pop()
        if next == cn:
            return cc

        for nn in graph[cn]:
            if nn not in visited:
                stack.append([nn, cc+1])
                visited.append(nn)
    return 0
def sol():
    N = int(input())
    num_list = list(map(int, input().split()))
    graph = {i+1:[] for i in range(N)}
    graph_dfs = {i+1:[] for i in range(N)}

    for i in range(len(num_list)):
        graph[num_list[i]].append(i+2)
        graph_dfs[num_list[i]].append(i+2)
        graph_dfs[i+2].append(num_list[i])

    cnt = 0
    queue = deque()
    queue.append(1)
    before = 1
    while queue:

        current = queue.popleft()
        if current in graph[before]:
            cnt += 1
        else:
            cnt += dfs(graph_dfs, before, current)

        before = current
        for next in graph[current]:
            queue.append(next)
    return cnt

answer_list = []
for i in range(T):
    answer_list.append(sol())
for i, a in enumerate(answer_list):
    print("#{} {}".format(i+1, a))






