
from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        # 1 : 1 1가지
        # 2 : 1+1, 2  2가지
        # 3 : 1+1+1, 2+1 2가지
        # 4 : 1+1+1+1, 2+1+1, 2+2 3가지
        # 5 : 1+1+1+1+1, 2+1+1+1, 2+2+1, 5 4가지

        len_coins = len(coins)
        d = [0] * (amount + 1) # amount에 대한 코인으로 만들수 있는 경우의 수
        d[0] = 1
        for j in range(len_coins):
            for i in range(1, amount + 1):
                if (i - coins[j]) >= 0:
                    d[i] += d[i - coins[j]]

        return d[amount]

amount = 5
coins = [1,2,5]
# output : 4
answer = Solution().change(amount, coins)
print(answer)