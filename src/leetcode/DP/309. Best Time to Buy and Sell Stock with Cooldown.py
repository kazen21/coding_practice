from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i] # 파는 경우 다음날은 cooldown이므로 i+2 에 다시 살 수 있다.
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]

        result = dfs(0, True)
        return result
######################################################################################33

# from typing import List
#
#
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l = len(prices)
#         dp: List[int] = [0] * l
#
#         for idx_sell in range(1, l):
#             for idx_buy in range(0, idx_sell):
#                 profit = prices[idx_sell] - prices[idx_buy]
#
#                 if idx_buy - 2 > 0:
#                     profit += dp[idx_buy - 2]
#
#                 dp[idx_sell] = max(dp[idx_sell], profit)
#
#             dp[idx_sell] = max(dp[idx_sell], dp[idx_sell - 1])
#
#         return dp[len(prices) - 1]


prices = [1,2,3,0,2]
# output : 3
answer = Solution().maxProfit(prices)
print(answer)
