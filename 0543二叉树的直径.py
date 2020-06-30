# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max_size = 0
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 递归，和计算树的高度有点类似
        # 好像在百度面试的时候被问到过，当时明确表示：
        # 爷8会 p(´⌒｀｡q)
        self.max_size = 0
        def helper(root):
            if not root:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            self.max_size = max(self.max_size, l+r)

            return max(l, r) + 1
        
        helper(root)
        return self.max_size