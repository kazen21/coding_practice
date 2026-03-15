from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(remain: int, start_idx: int, path: List[int]):

            if remain == 0:
                result.append(list(path))
                return


            if remain < 0:
                return

            for i in range(start_idx, len(candidates)):
                path.append(candidates[i])
                backtrack(remain - candidates[i], i, path)
                path.pop()


        backtrack(target, 0, [])
        return result


