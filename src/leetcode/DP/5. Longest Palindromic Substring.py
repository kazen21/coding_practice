
class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        for length in range(n, 0, -1):
            left = 0
            right = length - 1

            while right < n:
                if self.check_palindrome(left, right, s):
                    return s[left:right+1]
                left += 1
                right += 1

    def check_palindrome(self, left, right, s):

        for i in range((right-left)//2 +1):
            if s[left+i] != s[right-i]:
                return False
        return True

s = "babad"
answer = Solution().longestPalindrome(s)
print(answer)
# output = "bab"