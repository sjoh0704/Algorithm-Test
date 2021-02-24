s = input()
case1 = s.split("0")
case2 = s.split("1")
cnt = 0
cnt2 = 0
for i in case1:
    if i != '':
        cnt += 1
for i in case2:
    if i != '':
        cnt2 += 1
if cnt2 > cnt:
    print(cnt)
else:
    print(cnt2)
