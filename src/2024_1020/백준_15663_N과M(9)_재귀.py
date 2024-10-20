

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def solve():
    n, choice = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    # n, choice = 4, 4
    # a = [1,1,1,1]
    # a = list(set(a))
    a.sort()

    # print(a)
    n = len(a)
    visited = [0]*n
    data = set()
    def go(L, selected):
        if L == choice:
            # print(selected)
            val = ' '.join(map(str, selected))
            if val not in data:
                data.add(val)
                print(val)
                return
            return
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                go(L+1, selected + [a[i]])
                visited[i] = 0
    go(0, [])

solve()