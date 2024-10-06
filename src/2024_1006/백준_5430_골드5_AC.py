
import sys
from collections import deque
input = sys.stdin.readline

def solve():
    ans = []
    t = int(input().strip())

    for _ in range(t):
        p = input().strip()
        n = int(input().strip())
        arr = list(input().strip()[1:-1].split(','))
        q = deque(arr)
        error = 0
        reverse = False
        if n == 0:
            q = []

        for c in p:
            if c == "R":
                # q.reverse() #시간 초과로 사용 할 수 없다
                reverse = not reverse
            elif c == "D":
                if len(q) == 0:
                    # print("error")
                    error = 1
                    break
                else:
                    if reverse == True:
                        q.pop()
                    else:
                        q.popleft()

        if error == 1:
            print("error")
            continue
        else:
            if reverse:
                q.reverse()
        ans = '['+ ','.join(q) +']'
        print(ans)

solve()