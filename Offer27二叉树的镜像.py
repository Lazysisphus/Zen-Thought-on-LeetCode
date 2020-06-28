# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 空树
        if not root:
            return root
        # 当前结点是叶子结点
        if not root.left and not root.right:
            return root
        # 交换左右子树
        root.left, root.right = root.right, root.left
        # 递归
        if root.left:
            self.mirrorTree(root.left)
        if root.right:
            self.mirrorTree(root.right)
        return root