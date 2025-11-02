

from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def bfs(sr, sc):
            q = deque([(sr, sc)])
            board[sr][sc] = 'T' 
            while q:
                r, c = q.popleft()
                for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                        board[nr][nc] = 'T'
                        q.append((nr, nc))

        # 상하 경계
        for c in range(n):
            if board[0][c] == 'O':
                bfs(0, c)
            if board[m-1][c] == 'O':
                bfs(m-1, c)

        # 좌우 경계
        for r in range(m):
            if board[r][0] == 'O':
                bfs(r, 0)
            if board[r][n-1] == 'O':
                bfs(r, n-1)

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'

