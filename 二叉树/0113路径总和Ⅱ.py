# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(node, tmp, tmp_sum):
            if not node:
                return 
            if not node.left and not node.right and tmp_sum + node.val == sum:
                res.append(tmp + [node.val])
                return
            dfs(node.left, tmp + [node.val], tmp_sum + node.val)
            dfs(node.right, tmp + [node.val], tmp_sum + node.val)
        res = []
        dfs(root, [], 0)
        return res