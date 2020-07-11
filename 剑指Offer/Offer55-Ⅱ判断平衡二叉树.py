# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 递归后序遍历，从底向上，通过剪枝避免了重复的计算
        # 本题的最优解法
        # 时间复杂度O(n)，空间复杂度O(n)
        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            if left == -1: # -1返回值表示以左节点为根的子树不是平衡二叉树
                return -1 # 剪枝
            right = depth(root.right)
            if right == -1:
                return -1
            return max(left, right) + 1 if abs(left - right) <= 1 else -1
        return depth(root) != -1

        # 递归先序遍历，计算树的深度，然后判断
        # 从顶向下的遍历，会有重复的计算
        # 时间复杂度O(nlogn)，空间复杂度O(n)
        def depth(root):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            h = max(left, right) + 1
            return h
        
        if not root:
            return True
        left = depth(root.left)
        right = depth(root.right)
        return abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)