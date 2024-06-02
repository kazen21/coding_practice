
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float('inf')] * (n+1)

        for i in range(n+1):
            if i == 0:
                dp[0] = 0
            elif i == 1:
                dp[1] = 0
            else:
                # dp[3] = dp[2]+cost[2], dp[1]+cost[1]
                dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])

        # print(dp)
        return dp[n]


cost = [10,15,20]
answer = Solution().minCostClimbingStairs(cost)
print(answer)