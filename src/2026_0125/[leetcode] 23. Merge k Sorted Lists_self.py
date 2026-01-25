import heapq
from typing import List, Optional


# LeetCode의 노드 정의 (로컬 테스트용)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # print(lists)
        min_heap = []

        for i, lst in enumerate(lists):

            if lst:
                print(i, lst.val, lst)
                heapq.heappush(min_heap, (lst.val, i, lst))


        dummy = ListNode(0)
        # print("dummy", dummy)
        curr = dummy

        while min_heap:
            #  (val: 값, i: 인덱스, node: 노드 객체) : 가장 작은 노드
            val, i, node = heapq.heappop(min_heap)

            # 결과 리스트에 연결
            curr.next = node
            curr = curr.next

            #다음 노드가 있다면 힙에 넣는다.
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        # 시작점 반환
        return dummy.next
