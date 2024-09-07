

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [-1,1,0,0]
dirX = [0,0,-1,1]

def dfs(y, x):
    global map_
    map_[y][x] = False

    for i in range(4):
        newY = y+dirY[i]
        newX = x+dirX[i]
        if map_[newY][newX]:
            dfs(newY, newX)


T = int(input())

# MAX = 50 + 10

while T > 0:
    T -= 1

    M,N,K = map(int, input().split())
    map_ = [[False]*(M+1) for _ in range(N+1)]
    # visited = [[False]*MAX for _ in range(MAX)]

    for _ in range(K):
        x, y = map(int, input().split())
        map_[y][x] = True

    answer = 0
    for i in range(N):
        for j in range(M):
            if map_[i][j]:
                dfs(i,j)
                answer += 1

    print(answer)
