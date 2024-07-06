
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        len_t1 = len(text1)
        len_t2 = len(text2)

        dp = [[0]*(len_t2+1) for _ in range(len_t1+1)]

        for i in range(1, len_t1+1):
            for j in range(1, len_t2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

text1 = "abcde"
text2 = text2 = "ace"
# output : 3
answer = Solution().longestCommonSubsequence(text1, text2)
print(answer)

