
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        ans = 0
        prev_end = -int(1e15)

        for x, y in intervals:
            if x >= prev_end:
                prev_end = y
            else:
                ans += 1

        return ans