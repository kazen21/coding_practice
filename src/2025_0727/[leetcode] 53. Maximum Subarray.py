# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        currsub = 0
        maxsub = nums[0]

        for num in nums:
            if currsub < 0:
                currsub = 0
            currsub += num
            maxsub = max(maxsub, currsub)

        return maxsub