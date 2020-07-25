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
        def helper(node1, node2):
            if not node1 and not node2: # 两个结点都不存在
                return True
            elif not node1 or not node2: # 只存在一个结点
                return False
            elif node1.val != node2.val: # 两个结点都存在，但是值不相同
                return False
            return helper(node1.left, node2.right) and helper(node1.right, node2.left)
        return helper(root, root)