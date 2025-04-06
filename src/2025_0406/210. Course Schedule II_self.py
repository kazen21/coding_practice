
# 위상정렬
from typing import List
from collections import defaultdict
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        # 선수 과목 관계를 그래프에 추가
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        queue = deque()
        for node in range(numCourses):
            if in_degree[node] == 0:
                queue.append(node)

        result = []
        while queue:
            cur_node = queue.popleft()
            result.append(cur_node)

            for next in graph[cur_node]:
                in_degree[next] -= 1

                if in_degree[next] == 0:
                    queue.append(next)

        if len(result) == numCourses:
            return result
        else:
            return []

if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0]]

    sol = Solution()
    print(sol.findOrder(numCourses, prerequisites))