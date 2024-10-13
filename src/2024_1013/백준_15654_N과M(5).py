

import sys
input = sys.stdin.readline

def solve():

    n, m = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))

    nums.sort()

    data = [0] * m
    visited = [False] * (n)

    def rec(L, n, m):
        if L == m:
            print(' '.join(map(str, data)))
            return
        for i in range(n):
            if visited[i] == True:
                continue
            visited[i] = True
            data[L] = nums[i]
            rec(L + 1, n, m)
            visited[i] = False

    rec(0, n, m)

solve()
