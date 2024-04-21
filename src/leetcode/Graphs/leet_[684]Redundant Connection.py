from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range( n +1)]
        # print(parent)
        rank = [1 ] *( n +1)

        def find(v):
            if parent[v] == v:
                return v
            parent[v] = find(parent[v])
            return parent[v]

        def union(v1, v2):
            v1_root = find(v1)
            v2_root = find(v2)

            if v1_root == v2_root:
                return False

            if rank[v1_root] < rank[v2_root]:
                parent[v1_root] = v2_root
            elif rank[v1_root] > rank[v2_root]:
                parent[v2_root] = v1_root
            else:
                parent[v2_root] = v1_root
                rank[v1_root] += 1
            return True


        for v1, v2 in edges:
            if not union(v1, v2):
                return [v1, v2]
