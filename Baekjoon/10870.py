num = int(input())

def pivo(num):
    if num == 0:
        print('0')
        return
    pivo = [0 for _ in range(num+1)]
    pivo[1] = 1
    for i in range(2, num+1):
        pivo[i] = pivo[i-1] + pivo[i-2]
    print(pivo[num])
pivo(num)