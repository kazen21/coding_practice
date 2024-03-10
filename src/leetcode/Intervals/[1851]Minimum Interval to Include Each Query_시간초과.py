from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        dict = {}
        intervals.sort()

        for q in queries:
            hq = []
            for idx, interval in enumerate(intervals):
                left, right = interval

                if left<=q<=right:
                    l = right - left + 1
                    heapq.heappush(hq, [l,q])

            if len(hq) > 0:
                _l, _q = heapq.heappop(hq)
                dict[_q] = _l
            else:
                dict[q] = -1


        # print(dict)
        return [dict[q] for q in queries]