
from collections import deque
import sys

input = sys.stdin.readline

# 모든 지점에서 목표지점까지의 거리를 구하기 위해 각각 지점을 start 로 하면 start가 여러개 생겨 복잡해진다
# 따라서 목표지점을 start 로 하나로 바꾸고, bfs 로 간 지점을 각 지점의 거리로 계산한다.

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solve(n, m, board):
    distance = []

    x_start, y_start = 0, 0
    for i in range(n):
        distance.append([])
        for j in range(m):
            if board[i][j] == 0: #갈수 없는 땅
                distance[i].append(0)
            elif board[i][j] == 1: #갈수 있는 땅
                distance[i].append(-1) # 갈 수 있는 땅이지만, 도달할 수 없으면 -1 이므로 default -1

            elif board[i][j] == 2: # 목표지점
                x_start, y_start = i, j #목표지점을 start로 변경한다. 즉 목표지점에서 각 지점의 거리를 구하기 위해
                distance[i].append(0)

    def bfs(x, y):
        q = deque()
        q.append((x, y))

        while q:
            cx, cy = q.popleft()

            for k in range(len(dx)):
                nx = cx + dx[k]
                ny = cy + dy[k]

                if 0<=nx<n and 0<=ny<m and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[cx][cy] + 1
                    q.append((nx,ny))

    bfs(x_start, y_start)

    for i in range(n):
        for j in range(m):
            print(distance[i][j], end=' ')
        print()


# 15 15
# 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
# 1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
# 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1

n, m = map(int, input().strip().split())

board = []
for _ in range(n):
    data = list(map(int, input().strip().split()))
    board.append(data)

solve(n,m,board)