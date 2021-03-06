import sys
read = sys.stdin.readline
N = int(input())
get_list = []
for _ in range(N):
    get_list.append(int(input()))

get_list.sort(reverse=True)

for i in get_list:
    print(i, end=" ")
