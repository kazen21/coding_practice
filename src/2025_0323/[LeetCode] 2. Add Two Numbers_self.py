from typing import Optional


# 연결 리스트 노드 정의
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self):

        return f"ListNode(val={self.val}, next={self.next})"


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # print(l1)

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # 각 노드의 값과 올림수를 더함
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            carry = total // 10
            current.next = ListNode(total % 10)

            # 다음 노드로 이동
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

if __name__ == "__main__":
    # l1 = [2,4,3]
    # l2 = [5,6,4]

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    sol = Solution()
    print(sol.addTwoNumbers(l1, l2))