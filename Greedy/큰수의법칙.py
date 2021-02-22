import sys
read = sys.stdin.readline
N, M ,K = map(int, read().split())
get_list = list(map(int, read().split()))
sorted_list = sorted(get_list, reverse=True)

# 방법 1

# sum = 0
# for i in range(1, M+1):
#     if i % (K+1) == 0:
#         sum += sorted_list[1]
#     else:
#         sum += sorted_list[0]
# print(sum)

# 방법 2

cnt = M // (K+1)
sum = sorted_list[0]*(M-cnt) + sorted_list[1]*cnt
print(sum)
