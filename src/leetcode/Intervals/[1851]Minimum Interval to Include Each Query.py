from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        length = len(intervals)
        intervals.sort()
        heap = []
        dict = {}
        idx = 0

        for q in sorted(queries):

            #left 값중 q보다 작은 값들의 (right-left-1) 를 계산해서 넣는다.
            while idx < length and intervals[idx][0] <= q:
                left, right = intervals[idx]
                l = right - left + 1
                heapq.heappush(heap, [l, right])
                idx += 1

            #heap에 들어있는 값중 right가 더 작으면 heap에서 제거
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            #(right-left-1) 이 가장 작은 값을 dict 에 넣는다
            dict[q] = heap[0][0] if heap else -1

        return [dict[q] for q in queries]