import sys
read = sys.stdin.readline
N = int(input())
dic = {}
for _ in range(N):
    name, grade = read().split()
    dic[name] = int(grade)
sorted_dic = sorted(dic.items(), key=lambda x:x[1])
for i in range(N):
    print(sorted_dic[i][0], end=" ")

