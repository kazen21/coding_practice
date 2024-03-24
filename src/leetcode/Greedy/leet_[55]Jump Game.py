from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        elm = 0

        # 현재 index에서 갈수있는 최대 값을 갱신한다.
        for idx, val in enumerate(nums):

            if elm < idx:
                return False

            elm = max(elm, val + idx)

        return True
