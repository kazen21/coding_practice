
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n

        for i in range(0, n):
            if i == 0:
                dp[0] = nums[0]
            elif i == 1:
                dp[1] = max(nums[1], nums[0]) #case [2, 1]
            else:
                # dp[2] = max(dp[0] + nums[2], dp[1])
                dp[i] = max(nums[i]+dp[i-2], dp[i-1])
        return dp[n-1]


nums = [1,2,3,1]
answer = Solution().rob(nums)
print(answer)