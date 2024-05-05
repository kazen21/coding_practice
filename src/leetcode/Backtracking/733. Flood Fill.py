from typing import List
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # print("yoo")
        n = len(image)
        m = len(image[0])

        choice_color = image[sr][sc]
        visited = [[False]*m for _ in range(n)]
        def bfs(x, y):
            q = deque()
            q.append((x,y))
            image[x][y] = color
            visited[x][y] = True
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]

            while q:
                px, py = q.popleft()

                for k in range(len(dx)):
                    nx = px + dx[k]
                    ny = py + dy[k]

                    if 0<=nx<n and 0<=ny<m and image[nx][ny] == choice_color  \
                        and visited[nx][ny] == False :
                        visited[nx][ny] = True
                        q.append((nx,ny))
                        image[nx][ny] = color

        bfs(sr,sc)
        # print(image)
        return image



image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
output = [[2,2,2],[2,2,0],[2,0,1]]
answer = Solution().floodFill(image, sr, sc, color)
print(answer)
