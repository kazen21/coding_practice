
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        dp1 = [0]*n
        if n < 2:
            return nums[0]

        dp1[0] = nums[0]
        dp1[1] = nums[0]

        for i in range(2, n-1):
            dp1[i] = max(dp1[i-1], dp1[i-2]+nums[i])

        dp2 = [0]*n
        dp2[0] = 0
        dp2[1] = nums[1]

        for i in range(2, n):
            dp2[i] = max(dp2[i-1], dp2[i-2]+nums[i])

        answer = max(max(dp1), max(dp2))

        return answer


nums = [0]
answer = Solution().rob(nums)
print(answer)
