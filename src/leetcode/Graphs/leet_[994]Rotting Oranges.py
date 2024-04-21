from typing import List
from collections import deque
import copy

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
        # visited = [[0] * C for _ in range(R)]

        minutes = 0

        # q_new = deque()

        def bfs():
            nonlocal fresh_cnt, minutes, q_rotten
            q_new = deque()
            # print(q_rotten)
            # return
            while q_rotten:
                sx, sy = q_rotten.popleft()

                # if fresh_cnt == 0:
                #     return visited[sx][sy]

                for k in range(len(dy)):
                    nx = sx + dx[k]
                    ny = sy + dy[k]

                    if 0 <= nx < R and 0 <= ny < C:
                        if grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            fresh_cnt -= 1
                            # visited[nx][ny] = visited[sx][sy] + 1
                            q_new.append((nx, ny))

                if len(q_rotten) == 0 and len(q_new) > 0:
                    q_rotten = copy.deepcopy(q_new)
                    q_new.clear()
                    minutes += 1

            return minutes

        answer = bfs()
        if fresh_cnt == 0:
            return answer
        return -1


###############################################################
# 잘못 풀이 : 2 가 여러개 일 때 고려가 안됨
# from typing import List
# from collections import deque
#
# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         answer = 0
#         R = len(grid)
#         C = len(grid[0])
#         q_rotten = deque()
#         fresh_cnt = 0
#         rotten_cnt = 0
#         for i in range(R):
#             for j in range(C):
#                 if grid[i][j] == 2:
#                     q_rotten.append((i, j))
#                     rotten_cnt += 1
#                 elif grid[i][j] == 1:
#                     fresh_cnt += 1
#
#         if fresh_cnt == 0:
#             return 0
#
#         if rotten_cnt == 0:
#             return -1
#
#         dx = [-1, 0, 1, 0]
#         dy = [0, 1, 0, -1]
#         visited = [[0] * C for _ in range(R)]
#
#         def bfs():
#             nonlocal fresh_cnt
#
#             while q_rotten:
#                 sx, sy = q_rotten.popleft()
#                 if fresh_cnt == 0:
#                     return visited[sx][sy]
#
#                 for k in range(len(dy)):
#                     nx = sx + dx[k]
#                     ny = sy + dy[k]
#
#                     if 0 <= nx < R and 0 <= ny < C and visited[nx][ny] == 0:
#                         if grid[nx][ny] == 1:
#                             grid[nx][ny] = 2
#                             fresh_cnt -= 1
#                             visited[nx][ny] = visited[sx][sy] + 1
#                             q_rotten.append((nx, ny))
#
#             return -1
#         answer = bfs()
#         return answer