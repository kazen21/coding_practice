from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, min_val, max_val):

            if not node:
                return True

            if not (min_val < node.val < max_val):
                return False

            left = validate(node.left, min_val, node.val)
            right = validate(node.right, node.val, max_val)

            if left == True and right == True:
                return True
            else:
                return False

        ret = validate(root, float('-inf'), float('inf'))
        return ret

