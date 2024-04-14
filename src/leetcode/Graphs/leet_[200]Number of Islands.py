from typing import List
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])

        answer = 0

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1':
                    q = deque()
                    q.append((i,j))
                    grid[i][j] = 0
                    answer += 1

                    while q:
                        px, py = q.popleft()

                        for k in range(4):
                            nx = px + dx[k]
                            ny = py + dy[k]

                            if 0<=nx<R and 0<=ny<C and grid[nx][ny] == '1':
                                q.append((nx,ny))
                                grid[nx][ny] = 0
        return answer