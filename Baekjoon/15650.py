import sys
from itertools import combinations

# 방법1. combination 모듈 이용 
def sol1(n, m):

    # 조합 생성
    com = list(combinations(list(range(1, n+1)), m))
    
    # 이쁘게 출력 
    for c in com:
        for t in c:
            print(t, end=' ')
        print()


# 방법2. 리커전을 이용
def sol2(n, m, ls=[0]): # list 초기에 0값을 넣어서 처음에 비교하는 경우를 생략 

    # 0을 포함한 리스트의 길이가 m+1이면 리커젼 종료 
    if len(ls) == m+1:

        # 이쁘게 출력
        for i in range(1, len(ls)):
            print(ls[i], end=' ')
        print()
        return 

    for i in range(1, n+1):

        # 이전 값보다 큰 경우에만 리커젼 시행 
        if ls[-1] < i:
            ls.append(i)
            sol2(n, m, ls)
            ls.pop()


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    sol2(N, M) 