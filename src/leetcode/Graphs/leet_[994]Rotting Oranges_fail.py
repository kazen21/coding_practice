from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        answer = 0
        R = len(grid)
        C = len(grid[0])
        q_rotten = deque()
        fresh_cnt = 0
        rotten_cnt = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    q_rotten.append((i, j))
                    rotten_cnt += 1
                elif grid[i][j] == 1:
                    fresh_cnt += 1

        if fresh_cnt == 0:
            return 0

        if rotten_cnt == 0:
            return -1

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        visited = [[0] * C for _ in range(R)]

        def bfs():
            nonlocal fresh_cnt

            while q_rotten:
                sx, sy = q_rotten.popleft()
                if fresh_cnt == 0:
                    return visited[sx][sy]

                for k in range(len(dy)):
                    nx = sx + dx[k]
                    ny = sy + dy[k]

                    if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0:
                        if grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            fresh_cnt -= 1
                            visited[nx][ny] = visited[sx][sy] + 1
                            q_rotten.append((nx, ny))

            return -1
        answer = bfs()
        return answer