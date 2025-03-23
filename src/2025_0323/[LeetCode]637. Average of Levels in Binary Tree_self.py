
from typing import List
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        # print(root)
        result = []
        q = deque()
        q.append(root)

        while q:
            cur_level_count = len(q)
            level_sum = 0

            for _ in range(cur_level_count):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            cur_node_avg = level_sum / cur_level_count
            result.append(cur_node_avg)

        return result

if __name__ == "__main__":
    # TreeNode
    # {val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode
    # {val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode
    # {val: 7, left: None, right: None}}}

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    sol = Solution()
    print(sol.averageOfLevels(root))



