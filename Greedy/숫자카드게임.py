import sys
read = sys.stdin.readline
N, M = map(int, read().split())
max_of_cards = 0
for _ in range(N):
    row = list(map(int, read().split()))
    min_row = min(row)
    max_of_cards = max(max_of_cards, min_row)
print(max_of_cards)


