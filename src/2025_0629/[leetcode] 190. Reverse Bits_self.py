


# -*- coding: utf-8 -*-

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            bit = n & 1  # 맨 오른쪽 비트 추출
            result = (result << 1) | bit  # result 왼쪽 밀고 새 비트 추가
            n >>= 1  # 오른쪽으로 밀어 다음 비트 준비
        return result
