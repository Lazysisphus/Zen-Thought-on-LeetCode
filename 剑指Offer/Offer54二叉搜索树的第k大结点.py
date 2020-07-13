# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # 和书上对“第k大”的定义略有不同
        # 使用二叉树中序遍历
        # 时间复杂度O(n)，空间复杂度O(n)
        def dfs(root):
            if not root:
                return 
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        
        res = []
        dfs(root)
        return res[-k]