# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []
        def backtrack(node, tmp):
            if not node:
                return 
            if not node.left and not node.right:
                res.append(tmp + "->" + str(node.val))
                return 
            if node.left:
                backtrack(node.left, tmp + "->" + str(node.val))
            if node.right:
                backtrack(node.right, tmp + "->" + str(node.val))
        backtrack(root, "")
        return [x[2: ] for x in res]