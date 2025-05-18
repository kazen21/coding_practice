

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        stock = Counter(magazine)
        print(stock)

        for ch in ransomNote:
            if stock[ch] == 0:
                return False
            stock[ch] -= 1
        return True


if __name__ == "__main__":
    ransomNote = "aa"
    magazine = "aab"
    sol = Solution()
    print(sol.canConstruct(ransomNote, magazine))