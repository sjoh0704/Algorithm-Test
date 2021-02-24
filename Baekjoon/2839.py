import sys
n = int(input())
five = n // 5
three = n // 3
ans = -1
for i in range(five, -1, -1):
    for j in range(three, -1, -1):
        if n == 5 * i + 3 * j:
            ans = i + j
            break
    if ans != -1:
        break
print(ans)

