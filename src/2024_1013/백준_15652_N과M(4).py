

import sys
input = sys.stdin.readline

def solve():

    n, m = map(int, input().strip().split())
    # n, m = 4, 2

    data = [0] * m
    visited = [False] * (n + 1)

    def rec(L, start, n, m):
        if L == m:

            print(' '.join(map(str, data)))
            return
        for num in range(start, n + 1):
            # if visited[num] == True:
            #     continue
            # visited[num] = True
            data[L] = num
            rec(L + 1, num, n, m)
            # visited[num] = False

    rec(0, 1, n, m)

solve()
