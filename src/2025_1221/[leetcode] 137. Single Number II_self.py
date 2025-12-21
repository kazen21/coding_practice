from typing import List
from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        counts = defaultdict(int)


        for num in nums:

            counts[num] += 1


        for key, value in counts.items():
            if value == 1:
                return key
