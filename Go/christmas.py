level = 10
rootLevel = 2
spaceNum = level -1

for i in range(1, level+1):
    spaceNum -= 1
    for j in range(0, spaceNum+1):
        print(' ', end='')
    for j in range(1, i*2):
        print("*", end='')
    print()

print("❤ Merry Christmas ❤")
for i in range(1, rootLevel+1):
    for j in range(1, level):
        print(" ", end='')
    print("*")