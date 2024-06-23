
from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        #dp[i] : i 번째 수가 가지는 LIS 최대 값
        dp = [1]*n #LIS는 최소 1개를 가지고 있음

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]: # 뒤에 수가 앞에 수보다 커야 함
                    dp[i] = max(dp[i], dp[j]+1)

        answer = max(dp)
        return answer

nums = [10,9,2,5,3,7,101,18]

answer = Solution().lengthOfLIS(nums)
print(answer)
