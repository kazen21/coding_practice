# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])

        copy_board = [row[:] for row in board]

        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        for x in range(m):
            for y in range(n):
                live = 0
                for dx, dy in dirs:
                    nx = x+dx
                    ny = y+dy
                    if 0 <= nx < m and 0 <= ny < n and copy_board[nx][ny] == 1:
                        live += 1
                if copy_board[x][y] == 1 and (live < 2 or live > 3):
                    board[x][y] = 0
                if copy_board[x][y] == 0 and live == 3:
                    board[x][y] = 1
