# -*- coding: utf-8 -*-

from typing import List

#Kadane's Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]

        for x in nums[1:]:
            cur_sum = max(x, cur_sum + x)
            max_sum = max(max_sum, cur_sum)

        return max_sum

if __name__ == "__main__":
    nums = [1,-2,3,-2]
    sol = Solution()
    print(sol.maxSubarraySumCircular(nums))