from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        # 같은 숫자 2개까지 허용
        if len(nums) <= 2:
            return len(nums)

        # k : 다음 유효한 숫자 위치
        k = 2

        for i in range(2, len(nums)):

            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k



# --- 테스트 예시 ---
solution = Solution()

# 예시 1
nums1 = [1, 2, 1, 2, 2, 3]
k1 = solution.removeDuplicates(nums1)
print(f"입력: [1, 1, 1, 2, 2, 3]")
print(f"결과 개수(k): {k1}")
print(f"수정된 배열(앞 k개): {nums1[:k1]}")
# 예상: k=5, [1, 1, 2, 2, 3]

print("-" * 20)

