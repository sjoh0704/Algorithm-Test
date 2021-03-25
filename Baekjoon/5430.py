import sys
from collections import deque
read = sys.stdin.readline

T = int(read())

def sol():
    func = list(read().strip())
    n = int(read())
    dir = True
    try:
        num_list = deque(map(int, read()[1:-2].split(",")))
        for i in range(len(func)):
            if func[i] == "R":
                dir = not dir

            elif func[i] == "D":
                if dir:
                    num_list.popleft()
                else:
                    num_list.pop()

    except Exception as e:
        print("error")
    else:
        if not dir:
            num_list.reverse()

        print(list(num_list))


for _ in range(T):
    sol()

