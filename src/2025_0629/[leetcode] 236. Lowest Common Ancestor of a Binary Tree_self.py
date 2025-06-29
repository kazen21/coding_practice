# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root: None}
        stack = [root]

        while p not in parent or q not in parent:  # 두 노드 모두 부모가 기록될 때까지
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # p 의 모든 조상 집합
        ancestors = set()

        while p:
            ancestors.add(p)
            p = parent[p]

        # q 를 따라 올라가며, p와 동일한 공통조상 찾기
        while q not in ancestors:
            q = parent[q]
        return q