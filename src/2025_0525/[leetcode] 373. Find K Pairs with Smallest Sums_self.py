
from typing import List
from heapq import heappush, heappop
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        answer = []
        hq = []
        n = min(k, len(nums2))
        for idx in range(n): # nums1은 0번 인덱스로 고정하고, nums2 의 모든 인덱스를 순회하면서 합을 구해서 힙에 넣어준다.
            heappush(hq, (nums1[0] + nums2[idx], 0, idx))

        #print(hq)
        ret = []
        cnt = 0
        while hq:
            _sum, i, j = heappop(hq)
            ret.append([nums1[i], nums2[j]])
            cnt += 1

            if cnt == k:
                return ret

            if i+1 < len(nums1): #num1 의 인덱스를 +1 하고, 현재 num2의 인덱스의 합을 힙에 넣는다. 즉 하나씩 인덱스를 증가시킨다.
                heappush(hq, (nums1[i+1] + nums2[j], i+1, j))

if __name__ == "__main__":

    nums1 = [1,7,11]
    nums2 = [2,4,6]
    k = 3
    # output = [[1,2],[1,4],[1,6]]
    sol = Solution()
    print(sol.kSmallestPairs(nums1, nums2, k))
