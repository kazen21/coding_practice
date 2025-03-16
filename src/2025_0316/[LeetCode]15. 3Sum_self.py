from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. 정렬
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum_val = nums[i] + nums[left] + nums[right]

                if sum_val < 0:
                    left += 1
                elif sum_val > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return result

if __name__ == "__main__":
    # Output: [[-1, -1, 2], [-1, 0, 1]]
    nums = [-1, 0, 1, 2, -1, -4]
    sol = Solution()
    print(sol.threeSum(nums))

