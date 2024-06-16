
from typing import List
import sys

INF = sys.maxsize

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [INF]*(amount+1)
        n = len(dp)

        # dp[i] : i를 만들 수 있는 최소 동전의 수
        # dp[3] : 맨 마지막 수 1 : dp[i-1] + 1, 맨마지막 수 2, dp[i-2] + 1, 맨 마지막 수 5 dp[i-5] + 1
        dp[0] = 0

        for i in range(1, n):
            for j in coins:
                if i - j >= 0:
                    dp[i] = min(dp[i], dp[i-j] + 1)

        answer = dp[amount]

        if answer == INF:
            return -1

        return answer



coins = [1,2,5]
amount = 11
answer = Solution().coinChange(coins, amount)
print(answer)