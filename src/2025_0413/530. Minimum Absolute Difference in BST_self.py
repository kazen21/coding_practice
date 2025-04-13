# Definition for a binary tree node (LeetCode에서 제공)
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        # 트리 노드의 값과 자식 여부를 문자열로 출력
        return f"TreeNode(val={self.val}, left={repr(self.left)}, right={repr(self.right)})"


INF = sys.maxsize
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:

        print(root)

        values = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)
        print(f"value={values}")


        min_diff = INF
        for i in range(1, len(values)):
            diff = values[i] - values[i - 1]
            if diff < min_diff:
                min_diff = diff

        return min_diff

if __name__ == "__main__":

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)

    root.left.left = TreeNode(1)
    root.left.righ = TreeNode(3)

    sol = Solution()
    print(sol.getMinimumDifference(root))
