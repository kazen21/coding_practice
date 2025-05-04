

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
import sys
sys.setrecursionlimit(10**7)
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(node , remaining):

            if not node :
                return False

            remaining -= node.val

            if not node.left and not node.right:
                return remaining == 0

            ret1 = dfs(node.left, remaining)
            ret2 = dfs(node.right, remaining)

            return ret1 or ret2

        result = dfs(root, targetSum)
        # print(result)
        return result

if __name__ == "__main__":

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    targetSum = 22
    sol = Solution()
    print(sol.hasPathSum(root, targetSum))
