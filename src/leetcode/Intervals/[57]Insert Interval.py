from typing import List
import heapq

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        heap = [ i for i in intervals] # 깊은 복사
        intervals.append(newInterval) # index error 방지

        #interval 과 newinterver 을 heapq 로 만듬
        heap = heap
        heapq.heapify(heap)
        heapq.heappush(heap, newInterval)

        #비교를 위한 정답 초기값
        answer = [intervals.pop(0)]

        while len(heap) > 0:
            a_start, a_end = answer.pop()
            b_start, b_end = heapq.heappop(heap)
            over_lapped = False

            # answer 와 heapq 비교 , 겹칠때와 안겹칠때
            if a_start <= b_start and b_end <= a_end:
                over_lapped = True
            elif b_start <= a_start and a_end <= b_end:
                over_lapped = True
            elif a_start <= b_start <= a_end:
                over_lapped = True
            elif a_start <= b_end <= a_end:
                over_lapped = True

            if over_lapped:
                start = min(a_start, b_start)
                end = max(a_end, b_end)
                answer.append([start, end])
            else:
                answer.append([a_start, a_end])
                answer.append([b_start, b_end])

            #마지막값이 큰값이 오도록
            answer.sort()

        return answer