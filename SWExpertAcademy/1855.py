from collections import deque


def findAncestor(graph, current, next):
    ca = []
    na = []

    while True:
        if len(graph[current]) == 0:
            break
        tmp = graph[current][0]
        ca.append(tmp)
        current = tmp
    while True:
        if len(graph[next]) == 0:
            break
        tmp = graph[next][0]
        na.append(tmp)
        next = tmp

    answer = 0
    for i, n in enumerate(na[::-1]):
        for j, c in enumerate(ca[::-1]):
            if n == c:
                answer = len(na)-i + len(ca)-j
                break

    return answer
def sol():
    N = int(input())
    num_list = list(map(int, input().split()))
    graph = {i+1:[] for i in range(N)}
    graph2 = {i+1:[] for i in range(N)}

    for i in range(len(num_list)):
        graph[num_list[i]].append(i+2)
        graph2[i+2].append(num_list[i])

    cnt = 0
    queue = deque()
    queue.append(1)
    before = 1
    while queue:

        current = queue.popleft()
        if current in graph[before]:
            tmp = 1
        else:
            tmp = findAncestor(graph2, before, current)

        cnt += tmp
        before = current
        for next in graph[current]:
            queue.append(next)
    return cnt

T = int(input())

answer_list = []
for i in range(T):
    answer_list.append(sol())
for i, a in enumerate(answer_list):
    print("#{} {}".format(i+1, a))

