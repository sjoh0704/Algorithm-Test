import sys
read = sys.stdin.readline
N = int(read())
num_list = []
for _ in range(N):
    num_list.append(int(read()))
def getMode(num_list):
    dic = {}
    for i in range(N):
        if num_list[i] not in dic:
            dic[num_list[i]] = 1
        else:
            dic[num_list[i]] += 1
    ans = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
    if len(ans) == 1:
        return ans[0][0]
    elif ans[0][1] == ans[1][1]:
        return ans[1][0]
    else:
        return ans[0][0]
print(round(sum(num_list)/N))
print(sorted(num_list)[N//2])
print(getMode(num_list))
print(max(num_list) - min(num_list))