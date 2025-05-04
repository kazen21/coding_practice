from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc", "3": "def",  "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        ans = []

        def backtrack(idx, path):
            if idx == len(digits):
                ans.append(path)
                return

            for ch in phone[digits[idx]]: # 2: "abc", 3:"def"
                backtrack(idx + 1, path + ch)

        backtrack(0, "")
        return ans

if __name__ == "__main__":
    digits = "23"
    sol = Solution()
    print(sol.letterCombinations(digits))