n = int(input())
# 방법1
sum = 0
for i in range(n+1):
    if "3" in str(i):
       sum += 3600
    else:
        sum += 1575
print(sum)

# 방법2

sum = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) + str(j) + str(k):
                sum += 1
print(sum)

