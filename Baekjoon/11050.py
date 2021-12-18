import sys

def sol(n, k):
    if k == 0 or n == k:
        return 1
    elif k == 1:
        return n
    
    return sol(n-1, k-1) + sol(n-1, k)

if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    print(sol(n, k))    
    
