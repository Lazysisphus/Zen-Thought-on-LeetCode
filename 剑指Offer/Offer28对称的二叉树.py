# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(root1, root2):
            if root1 == None and root2 == None:
                return True
            elif root1 == None or root2 == None:
                return False
            # 递归
            if root1.val != root2.val:
                return False
            return helper(root1.left, root2.right) and helper(root1.right, root2.left)
        return helper(root, root)