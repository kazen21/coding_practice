
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        total_cnt = 0
        for i in range(n):
            total_cnt += self.check_palindrome(i, i, s)
            total_cnt += self.check_palindrome(i, i+1, s)

        return total_cnt

    def check_palindrome(self, left, right, s):
        count = 0
        while left >=0 and right < len(s):
            if s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            else:
                break
        return count

s = "aaa"
answer = Solution().countSubstrings(s)
print(answer)
# answer = 6