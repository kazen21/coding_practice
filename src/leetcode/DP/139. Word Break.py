
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # 문자열 s 의 index의 매칭 여부
        # 예) dp[3] : s[0]~s[3] 까지의 매칭 성공
        dp = [False] * (len(s)+1)
        dp[0] = True

        for i in range(len(s)): # s의 index
            if dp[i] == False:
                continue
            print(i)
            for j in range(len(wordDict)):
                word = wordDict[j]
                cnt = 0
                for k in range(len(word)): #문자열 s 와 word 비교
                    if i+k < len(s) and word[k] != s[i+k]: #s의 범위 초과 주의
                        cnt = -1
                        break
                    cnt += 1
                if cnt != -1 and i+cnt < len(s) + 1 :#dp 의 범위 초과 주의
                    dp[i+cnt] = True

        # print(dp)
        return dp[-1]


# s = "leetcode"
# wordDict = ["leet","code"]

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]


answer = Solution().wordBreak(s, wordDict)
print(answer)

