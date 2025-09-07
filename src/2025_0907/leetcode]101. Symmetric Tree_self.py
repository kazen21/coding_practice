
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def mirror(a, b):
            # 둘 다 없으면 대칭
            if not a and not b:
                return True
            # 하나만 없으면 대칭 아님
            if not a or not b:
                return False
            # 값이 다르면 대칭 아님
            if a.val != b.val:
                return False

            return mirror(a.left, b.right) and mirror(a.right, b.left)

        return mirror(root.left, root.right)


