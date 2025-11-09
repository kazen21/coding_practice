from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        if n == 0:
            return 0

        # triangle과 동일한 삼각형 모양의 dp 만들기
        dp = [[0] * (i + 1) for i in range(n)]

        # 바닥(마지막 행)을 그대로 복사
        dp[-1] = triangle[-1][:]

        # 아래에서 위로 올라오며 갱신
        for i in range(n - 2, -1, -1):        # 마지막-1 행부터 0행까지
            for j in range(i + 1):            # 해당 행의 모든 칸
                dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])

        # 꼭대기가 최소 경로 합
        return dp[0][0]