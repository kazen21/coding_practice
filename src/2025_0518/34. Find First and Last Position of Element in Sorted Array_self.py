

# 이분탐색

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_pos() :
            left = 0
            right = len(nums) - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= target:
                    if nums[mid] == target:
                        res = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return res

        def last_pos() :
            left = 0
            right = len(nums) - 1
            res = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    if nums[mid] == target:
                        res = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return res

        first = first_pos()
        last = last_pos()
        return [first, last]

if __name__ == "__main__":

    nums = [5,7,7,8,8,10]
    target = 8
    sol = Solution()
    print(sol.searchRange(nums, target))