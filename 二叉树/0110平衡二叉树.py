# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 自顶向下扫描
    # 如果一棵树是平衡二叉树，那么除了要满足左右子树高度差小于2，还需要他的左右子树也是平衡二叉树
    # 时间复杂度O(nlogn)，空间复杂度O(n)
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.height(root.left) - self.height(root.right)) < 2

    def height(self, root):
        if not root:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        h = max(left, right) + 1
        return h
    
    # 自底向上扫描
    # helper()的返回值为-1，表明以当前结点为根结点的树不是平衡树
    # 时间复杂度O(n)，空间复杂度O(n)
    def isBalanced(self, root: TreeNode) -> bool:
        return False if self.helper(root) == -1 else True

    def helper(self, root):
        if not root:
            return 0
        left = self.helper(root.left)
        if left == -1:
            return -1 
        right = self.helper(root.right)
        if right == -1:
            return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1