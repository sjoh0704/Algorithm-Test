def sol():
    N, M = map(int ,input().split())
    compare = []
    answer = []
    if N == 1:
        answer.append('UNKNOWN')
        return answer

    for i in range(M):
        tmp = input().split()

        compare.append([tmp[0]]+list(map(int, tmp[1:])))

    result = ['x' for _ in range(N+1)]

    for i in range(len(compare)):
        if compare[i][0] == '!':
            if result[compare[i][1]] == 'x' and result[compare[i][2]] == 'x':
                result[compare[i][1]] = 0
                result[compare[i][2]] = compare[i][3] + result[compare[i][1]]
            elif result[compare[i][1]] == 'x':
                result[compare[i][1]] = result[compare[i][2]] - compare[i][3]
            elif result[compare[i][2]] == 'x':
                result[compare[i][2]] = result[compare[i][1]] + compare[i][3]
            else:
                continue

        else:
            if result[compare[i][1]] != 'x' and result[compare[i][2]] != 'x':
                answer.append(result[compare[i][2]] - result[compare[i][1]])

            else:
                answer.append("UNKNOWN")
    return answer


T = int(input().strip())
tmp = []
for i in range(T):
    tmp.append(sol())
for i in range(T):
    print("#{} {}".format(i+1, " ".join(map(str, tmp[i]))))

# from collections import defaultdict
#
#
# def find(a):
#     if not parent[a]:
#         return a
#     pa = parent[a]
#     parent[a] = find(pa)
#     weight[a] += weight[pa]
#     return parent[a]
#
#
# def union(a, b, w):
#     pa = find(a)
#     pb = find(b)
#     if pa == pb:
#         return
#     diff = weight[b] - weight[a]
#     if rank[pa] > rank[pb]:
#         pa, pb = pb, pa
#         w = -w
#         diff = -diff
#     weight[pa] = w + diff
#     parent[pa] = pb
#     if rank[pa] == rank[pb]:
#         rank[pb] += 1
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     parent = defaultdict(int)
#     weight = defaultdict(int)
#     rank = defaultdict(int)
#     ans = []
#     for _ in range(M):
#         work = input()
#         if work[0] == '!':
#             a, b, w = map(int, work.split()[1:])
#             union(a, b, w)
#         else:
#             a, b = map(int, work.split()[1:])
#             if find(a) == find(b):
#                 ans.append(weight[a] - weight[b])
#             else:
#                 ans.append('UNKNOWN')
#     print('#{} {}'.format(tc, ' '.join(map(str, ans))))