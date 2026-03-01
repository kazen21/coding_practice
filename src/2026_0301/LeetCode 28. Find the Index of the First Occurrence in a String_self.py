class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        h_len = len(haystack)
        n_len = len(needle)

        if n_len > h_len:
            return -1

        for i in range(h_len - n_len + 1):
            if haystack[i: i + n_len] == needle:
                return i

        return -1


if __name__ == "__main__":
    solution = Solution()

    print(f"Test 1: {solution.strStr('sadbutsad', 'sad')}")

    print(f"Test 2: {solution.strStr('leetcode', 'leeto')}")
