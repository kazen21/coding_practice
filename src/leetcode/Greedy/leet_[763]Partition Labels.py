

from typing import List
import collections

class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        d = collections.defaultdict(int)

        # key, value = (글자, indx)
        for i, c in enumerate(S):
            d[c] = i

        ans, left, right = [], -1, -1

        for i, c in enumerate(S):
            #가장 큰 index가 큰 글자를 기준으로 나눈다
            right = max(right, d[c])
            if i == right:
                ans.append(right-left)
                left = i
        return ans