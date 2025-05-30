

class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        max_len = 0
        idx_L = 0
        idx_R = 0

        def expand(l, r): ## 중간에서 부터 왼쪽, 오른쪽 양쪽을 팰린드롬인지 검사
            while 0 <= l - 1 and r + 1 < n and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1

            return [r - l + 1, l, r]

        for center in range(n):
            length, l, r = expand(center, center)
            if max_len < length:
                max_len = length
                idx_L = l
                idx_R = r

            if center + 1 < n and s[center] == s[center + 1]:  # 짝수
                length, l, r = expand(center, center+1)
                if max_len < length:
                    max_len = length
                    idx_L = l
                    idx_R = r

        ##print(max_len, idx_L, idx_R)
        answer = s[idx_L:idx_R + 1]

        return answer


if __name__ == "__main__":
    s = "babad"
    sol = Solution()
    print(sol.longestPalindrome(s))
