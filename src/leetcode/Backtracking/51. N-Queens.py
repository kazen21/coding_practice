from typing import List

import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        result = []
        cnt = 0
        board = [ ['.']*n for _ in range(n)]
        # board = [ ['.' for _ in range(n)] for _ in range(n)]
        # print(board)
        v1 = [0]*n  # 열
        v2 = [0]*(2*n) # 오른쪽 대각선
        v3 = [0]*(2*n) # 왼쪽 대각선

        def dfs(L, board):
            nonlocal result, cnt
            if L == n:
                cnt += 1
                result.append(copy.deepcopy(board))
                return
            for j in range(n):
                if v1[j] == v2[L+j] == v3[L-j] == 0:
                    v1[j] = v2[L+j] = v3[L-j] = 1
                    board[L][j] = 'Q'
                    dfs(L+1, board)
                    v1[j] = v2[L+j] = v3[L-j] = 0
                    board[L][j] = '.'

        dfs(0, board)

        for ans in result:
            str_ans = [''.join(elm) for elm in ans]
            # print(str_ans)

            answer.append(str_ans)

        return answer


n=4
answer = Solution().solveNQueens(n)
print(answer)
