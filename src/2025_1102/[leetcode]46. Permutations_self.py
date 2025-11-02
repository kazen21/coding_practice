


from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        visited = [False] * n
        path = []

        def dfs():

            if len(path) == n:
                res.append(path[:])
                return


            for i in range(n):
                if visited[i] == True:
                    continue
                visited[i] = True
                path.append(nums[i])

                dfs() 


                path.pop()
                visited[i] = False

        dfs()
        return res
