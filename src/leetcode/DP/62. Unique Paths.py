
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        #로봇의 시작위치와 끝위치가 같아도 갈수있는 방법은 1개이다.
        #따라서 모든 초기값을 1로 세팅
        dp = [[1]*(n) for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

m = 3
n = 7
# output : 28
answer = Solution().uniquePaths(m, n)
print(answer)