import sys
import time
read =sys.stdin.readline
r, c, k = map(int, read().split())
A = []
for _ in range(3):
    A.append(list(map(int, read().split())))


def sorting(array):
    maxCol = len(array[0])
    maxRow = len(array)
    resultRow = len(array)
    result = []
    if len(array) < len(array[0]):
        # C
        tmp_list = []
        for i in range(maxCol):
            tmp = {}
            
            for j in range(maxRow):
                if array[j][i] != 0 and array[j][i] in tmp:
                    tmp[array[j][i]] += 1
                elif array[j][i] != 0 and array[j][i] not in tmp:
                    tmp[array[j][i]] = 1
            tmp = sorted(tmp.items(), key=lambda x: (x[1], x[0]))
    
            resultRow = max(resultRow, len(tmp) * 2)
            sorted_tmp = []
            
            for t in tmp:
                sorted_tmp.append(t[0])
                sorted_tmp.append(t[1])
            tmp_list.append(sorted_tmp)
     
        result = [[0 for _ in range(maxCol)] for _ in range(resultRow)]
        for i in range(len(tmp_list)):
            for j in range(len(tmp_list[i])):
                result[j][i] = tmp_list[i][j]

    else:
        # R 
        for i, row in enumerate(array):
            result.append([])
            tmp = {}
            for c in row:
                if c != 0 and c in tmp:
                    tmp[c] += 1
                elif c != 0 and c not in tmp:
                    tmp[c] = 1
 
            tmp = sorted(tmp.items(), key=lambda x: (x[1], x[0]))
            for num, cnt in tmp:
                result[i].append(num)
                result[i].append(cnt)
            maxCol = max(maxCol, len(result[i]))
        for i in range(maxRow):
            if len(result[i]) < maxCol:
                tmp = [0] * (maxCol - len(result[i]))
                result[i].extend(tmp)
    return result[:100][:100]

result = A

ans = 0 
while 1:
    if ans > 100:
        print(-1)
        break
    if r <= len(result) and c <= len(result[0]):
        if result[r-1][c-1] == k:
            print(ans)
            break
    ans += 1
    result = sorting(result)

  