import sys

def sol(n, m, result=[]):
    
    # 모두 반복했을 때 끝
    if m == 0:
        if doubleCheck(result):

            # 이쁘게 출력
            for i in range(len(result)):
                print(result[i], end=' ')
            print()
        return 
    
    for i in range(1, n+1):
        if not doubleCheck(result):
            continue
        
        # 하나씩 추가
        result.append(i)

        # 리커전
        sol(n, m-1, result)

        # 해당 케이스가 끝나면 다시 원래대로
        result.pop()
        

# 중복 여부 검사 
def doubleCheck(ls):
    if len(set(ls)) == len(ls):
        return True
    return False


if __name__ =="__main__":
    N, M = map(int, sys.stdin.readline().split())
    sol(N, M)
