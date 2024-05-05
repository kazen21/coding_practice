from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        # path = [0]*n
        candidates.sort()
        def dfs(L, start, sum, path):
            nonlocal ans
            # if L == len(candidates) :
            #     return

            if sum == target:
                print(f"sum=target, path={path}")
                return path

            for i in range(start, n):
                # path += [candidates[i]]
                if sum < target:
                    temp= dfs(L + 1, i, sum + candidates[i], path + [candidates[i]])
                    if temp != None:
                        ans.append(temp)
            return
        dfs(0, 0, 0, [])
        # ans.append(rtn)
        return ans

# answer = Solution().combinationSum(candidates=[2,3,6,7], target=7)
answer = Solution().combinationSum(candidates=[2,3,5], target=8)
print(answer)