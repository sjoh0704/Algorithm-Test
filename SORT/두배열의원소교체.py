import sys
read = sys.stdin.readline
N, K = map(int, read().split())
first = list(map(int, read().split()))
second = list(map(int, read().split()))
first.sort()
second.sort(reverse=True)
answer = sum(first[K:]) + sum(second[:K])
print(answer)