

def find(dic, start, target, cnt=0):
    print("find!!!")
    print(start, target)

    for node in dic[start]:


        if node[0] == target:
            cnt += node[1]
            return cnt
        else:
            print("dd")
            if dic[node[0]] != node[0]:
                find(dic, node[0], target, cnt)

    return 0
def sol():
    N, M = map(int ,input().split())
    compare = []
    answer = []
    dic = {i+1: [] for i in range(N)}
    if N == 1:
        answer.append('UNKNOWN')
        return answer

    for i in range(M):
        tmp = input().split()

        compare.append([tmp[0]]+list(map(int, tmp[1:])))
    cnt = 0
    for i in range(len(compare)):
        cnt = 0
        if compare[i][0] == '!':
            dic[compare[i][1]].append([compare[i][2], compare[i][3]])
            dic[compare[i][2]].append([compare[i][1], -compare[i][3]])
        else:
            print("{}번째".format(i+1))
            cnt += find(dic, compare[i][1], compare[i][2])

    print(cnt)

sol()
# T = int(input().strip())
# tmp = []
# for i in range(T):
#     tmp.append(sol())
# for i in range(T):
#     print("#{} {}".format(i+1, " ".join(map(str, tmp[i]))))

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