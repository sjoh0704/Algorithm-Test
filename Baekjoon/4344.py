import sys
read = sys.stdin.readline
C = int(read())
case = []
for i in range(C):
    case.append(list(map(int, read().split())))
    
answer = []
for c in case:
    avg = sum(c[1:])/c[0]
    cnt = 0
    for grade in c[1:]:
        if grade > avg:
            cnt += 1
    answer.append(cnt/c[0] * 100)

for a in answer:
    print("{:.3f}%".format(a))
