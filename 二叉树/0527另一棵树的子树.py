# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool 
        """
        # 时间复杂度O(n)
        def isSameTree(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            return s.val == t.val and isSameTree(s.left, t.left) and isSameTree(s.right, t.right)

        if not s and not t:
            return True
        if not s or not t:
            return False
        return isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)