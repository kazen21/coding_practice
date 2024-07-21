
# 최소 편집 거리(Minimum Edit Distance) 알고리즘
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 and j == 0 :
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + 1
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + 1
                else :
                    if word1[i-1] == word2[j-1] :
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

        # print(dp[n][m])
        return dp[n][m]



# word1 = "horse"
# word2 = "ros"
# output = 3

word1 = "intention"
word2 = "execution"
# output = 5


answer = Solution().minDistance(word1, word2)
print(answer)