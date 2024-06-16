
from typing import List
import sys

INF = sys.maxsize

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = len(nums)
        min_dp = [INF] * n
        max_dp = [-INF] * n

        # min_dp[i] : i 번째의 product의 최소값
        # max_dp[i] : i 번째의 product의 최대값
        # 2 3  -2   4
        # 2 3 -12  -48
        # 2 6  -2   4

        min_dp[0] = nums[0]
        max_dp[0] = nums[0]

        for i in range(1, n):

            min_dp[i] = min(min_dp[i-1]*nums[i], nums[i], max_dp[i-1]*nums[i])
            max_dp[i] = max(min_dp[i-1]*nums[i], nums[i], max_dp[i-1]*nums[i])

        # print(min_dp)
        # print(max_dp)
        answer = max(max_dp)

        return answer

nums = [2,3,-2,4]
answer = Solution().maxProduct(nums)
print(answer)