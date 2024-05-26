from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        n = len(board)
        m = len(board[0])
        visited = [ [0]*m for _ in range(n)]

        def dfs(L,x,y,w_len):
            if L == w_len:
                return True
            for dx, dy in [(-1,0),(0,1),(1,0),(0,-1)]:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                    if board[nx][ny] == word[L] :
                        visited[nx][ny] = 1
                        if dfs(L+1,nx,ny,w_len) == True:
                            return True
                        visited[nx][ny] = 0

            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    if dfs(1,i,j,len(word)) == True:
                        return True
                    visited[i][j] = 0
        return False

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"
word = "ABCB"
answer = Solution().exist(board, word)
print(answer)