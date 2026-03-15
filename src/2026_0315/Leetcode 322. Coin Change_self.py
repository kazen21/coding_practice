from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        max_val = amount + 1
        dp = [max_val] * (amount + 1)


        dp[0] = 0

        for i in range(1, amount + 1):

            for coin in coins:

                if i >= coin:

                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == max_val:
            return -1

        return dp[amount]

