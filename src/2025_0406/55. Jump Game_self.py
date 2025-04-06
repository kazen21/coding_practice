
# 그리디 알고리즘

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):

            if i > max_reach:
                return False

            max_reach = max(max_reach, i + nums[i])

        return True

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    sol = Solution()
    print(sol.canJump(nums))

