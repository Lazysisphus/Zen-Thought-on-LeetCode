# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        # 递归 + 记忆化
        # root.val + rob(root.left.left) + rob(root.left.right) + \
        #   rob(root.right.left) + rob(root.right.right) VS \
        #   rob(root.left) + rob(root.right)
        hash_map = {}
        def helper(root):
            if not root:
                return 0
            if root in hash_map:
                return hash_map[root]
            ans1 = root.val
            if root.left:
                ans1 += helper(root.left.left) + helper(root.left.right)
            if root.right:
                ans1 += helper(root.right.left) + helper(root.right.right)
            ans2 = helper(root.left) + helper(root.right)
            hash_map[root] = max(ans1, ans2)
            return hash_map[root]
        return helper(root)

        # dp，使用长度为2的数组来表示当前结点的两种状态
        # state[0]表示以当前结点为根结点的子树，如果不偷当前结点，可以偷取的最大值
        # state[1]表示以当前结点为根结点的子树，如果偷取当前结点，可以偷取的最大值
        # 程序以递归的方式实现（在解决树的问题时多借助递归）
        def helper(root):
            if not root:
                return [0, 0]
            res = [0, 0]
            left = helper(root.left)
            right = helper(root.right)
            res[0] = max(left[0], left[1]) + max(right[0], right[1])
            res[1] = left[0] + right[0] + root.val
            return res
        res = helper(root)
        return max(res[0], res[1])