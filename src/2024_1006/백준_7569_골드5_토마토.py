from collections import deque
import sys
input = sys.stdin.readline

dz = [ 0, 0, 0, 0, 1,-1]
dx = [ 0, 0,-1, 1, 0, 0]
dy = [ 1,-1, 0, 0, 0, 0]

def solve():
    m, n, h = map(int, input().strip().split())
    # m, n, h = 4, 3, 2

    maps = []
    dist = [[[-1 for _ in range(m)] for _ in range(n) ] for _ in range(h) ]
    q = deque()

    for z in range(h):
        maps_1 = []
        for x in range(n):
            line = list(map(int, input().strip().split()))
            maps_1.append(line)
            for y in range(m):
                if maps_1[x][y] == 1:
                    dist[z][x][y] = 0
                    q.append((z,x,y))
        # print(maps_1)
        maps.append(maps_1)

    # [[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], [[1, 1, 1, 1], [-1, -1, -1, -1], [1, 1, 1, -1]]]
    # print(maps)

    while q:
        cz, cx, cy = q.popleft()

        for k in range(len(dx)):
            nz = cz + dz[k]
            nx = cx + dx[k]
            ny = cy + dy[k]

            if 0<=nz<h and 0<=nx<n and 0<=ny<m and maps[nz][nx][ny] == 0 and dist[nz][nx][ny] == -1:
                dist[nz][nx][ny] = dist[cz][cx][cy] + 1
                q.append((nz,nx,ny))

    # print(dist)
    # [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]]
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if maps[z][x][y] == 0 and dist[z][x][y] == -1:
                    ans = -1
                    print(ans)
                    exit()

    result = [ y for z in dist for x in z for y in x ]
    ans = max(result)
    print(ans)

solve()

# 4 3 2
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# -1 -1 -1 -1
# 1 1 1 -1

# 5 3 2
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 1 0 0
# 0 0 0 0 0