
import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    temp = [list(map(int, input().strip().split())) for _ in range(n)]
    # n, k = 4, 7
    # temp=[[6, 13], [4, 8], [3, 6], [5, 12]]

    w, v = zip(*temp)

    w = [0] + list(w)
    v = [0] + list(v)

    d = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            d[i][j] = d[i - 1][j]
            if j - w[i] >= 0:
                d[i][j] = max(d[i][j], d[i - 1][j - w[i]] + v[i])

    print(d[n][k])

solve()