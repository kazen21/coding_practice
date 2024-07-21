from typing import List

# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         ret = 0
#         def go(index, sum):
#             nonlocal ret
#             if index == len(nums):
#                 if sum == target:
#                     ret += 1
#                 return
#
#             go(index+1, sum + nums[index])
#             go(index+1, sum - nums[index])
#
#         go(0,0)
#
#         # print(ret)
#         return ret


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def backtrack(index, total):
            if index == len(nums):
                if total == target:
                    return 1
                else:
                    return 0

            if (index, total) in cache:
                return cache[(index, total)]

            cache[(index, total)] = ((backtrack(index+1, total+nums[index])) \
                                  + (backtrack(index+1, total-nums[index])))
            return cache[(index, total)]

        ret = backtrack(0, 0)
        return ret


nums = [1,1,1,1,1]
target = 3
answer = Solution().findTargetSumWays(nums, target)
print(answer)
