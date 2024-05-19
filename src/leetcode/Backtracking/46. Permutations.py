
# from typing import List
#
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         answer = []
#         visited = []
#         self.dfs(nums, [], answer, visited)
#         return answer
#
#     def dfs(self, nums, curr, answer, visited):
#         if len(curr) == len(nums):
#             answer.append(curr[:])
#             return
#         for num in nums:
#             # if num not in curr:
#             if num not in visited and num not in curr:
#                 visited.append(num)
#                 curr.append(num)
#                 self.dfs(nums, curr, answer, visited)
#                 curr.pop()
#                 visited.clear()
########################################################################

from typing import List
visited = []
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        # visited = []
        self.dfs(nums, [], answer)
        return answer

    def dfs(self, nums, curr, answer):
        global visited
        if len(curr) == len(nums):
            answer.append(curr[:])
            return
        for num in nums:
            # if num not in curr:
            if num not in visited and num not in curr:
                visited.append(num)
                curr.append(num)
                self.dfs(nums, curr, answer)
                curr.pop()
                visited.clear()

nums = [1,2,3]
answer = Solution().permute(nums)
print(answer)