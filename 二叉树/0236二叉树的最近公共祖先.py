# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 这道题很经典
        # 解题的关键点是第一行，递归终止的条件，即当前结点不存在或者当前结点为p或者q中的一个
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: # 如果左子树和右子树都没有返回结点，那么無最近公共结点
            return None
        if left and right: # 如果左子树和右子树都有返回结点，那么最近公共结点是root
            return root
        return left if not right else right # 如果只有左子树返回结点，那么左子树的返回值是最近公共结点；反之亦然