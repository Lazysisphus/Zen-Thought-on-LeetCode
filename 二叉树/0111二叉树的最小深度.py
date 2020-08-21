# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # [1, 2]用例的高度为2，需要设置条件来满足“叶子结点”的条件
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0 and right == 0:
            return 1
        if left == 0 or right == 0:
            return right + 1 if left == 0 else left + 1
        h = min(left, right) + 1
        return h