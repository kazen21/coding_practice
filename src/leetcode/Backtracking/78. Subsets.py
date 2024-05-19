from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        n = len(nums)
        for depth in range(n+1):
            self.dfs(0, [], n, nums, depth, answer)
        return answer

    def dfs(self, start, curr, n, nums, depth, answer):
        if len(curr) == depth:
            answer.append(curr[:])
            return

        for i in range(start, n):
            curr.append(nums[i])
            self.dfs(i+1, curr, n, nums,depth, answer)
            curr.pop()

nums = [1,2,3]
answer = Solution().subsets(nums)
print(answer)
