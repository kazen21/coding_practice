
from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def solve():
    m, n = map(int, input().strip().split())
    a = [list(map(int, input().strip().split())) for _ in range(n)]

    # m, n = (6, 4)
    # a = [[1, -1, 0, 0, 0, 0], [0, -1, 0, 0, 0, 0], [0, 0, 0, 0, -1, 0], [0, 0, 0, 0, -1, 1]]

    # print(f"m,n={m,n}")
    # print(f"a={a}")
    dist = [[-1] * m for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                q.append((i, j))
                dist[i][j] = 0

    # print(q)
    # print(dist)

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                    # a[nx][ny] = 1
    # print(dist)
    ans = max([max(row) for row in dist]) # 각 행에 대해 최대값을 뽑고 그중에 최대를 또 뽑는다.
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0 and dist[i][j] == -1:
                ans = -1
    print(ans)

solve()

# 6 4
# 1 -1 0 0 0 0
# 0 -1 0 0 0 0
# 0 0 0 0 -1 0
# 0 0 0 0 -1 1
