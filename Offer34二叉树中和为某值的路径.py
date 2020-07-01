# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        # 递归先序遍历+回溯
        # 时间复杂度O(n)，空间复杂度O(n)
        res = []
        path = []
        cur_sum = sum

        def helper(root, cur_sum):
            if not root:
                return
            
            path.append(root.val)
            cur_sum -= root.val
            if cur_sum == 0 and not root.left and not root.right:
                import copy
                res.append(copy.copy(path))
            if root.left:
                helper(root.left, cur_sum)
            if root.right:
                helper(root.right, cur_sum)
            path.pop()
            cur_sum += root.val

        helper(root, sum)
        return res