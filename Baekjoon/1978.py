import sys
from math import sqrt


# 소수임을 체크 
def checkPrime(n):
    if n < 2:
        return False

    # sqrt만큼 검사 
    for i in range(2, int(sqrt(n))+1):

        # 나누어진다면 소수가 아님
        if n % i == 0:
            return False
            
    return True


if __name__ == '__main__':
        
    read = sys.stdin.readline
    N = int(read())
    num = list(map(int, read().split()))
    ans = 0
    for n in num:
        if checkPrime(n):
            ans += 1
    print(ans)


