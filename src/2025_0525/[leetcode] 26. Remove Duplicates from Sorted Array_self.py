
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n-1, 0, -1):
            if nums[i] == nums[i-1]: # 뒤에서부터 계산하면 효율성이 증가
                nums.pop(i)
                cnt += 1

        # print(nums)

        return len(nums)



if __name__ == "__main__":
    nums = [1,1,2]
    sol = Solution()
    print(sol.removeDuplicates(nums))

