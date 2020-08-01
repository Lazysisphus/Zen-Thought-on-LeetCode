# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        # 递归，话不多说看代码
        def helper(start, end): # 函数返回[start, end]区间构造的所有二叉搜索树
            if start > end:
                return [None]
            
            all_trees = []
            for i in range(start, end + 1):
                left = helper(start, i - 1)
                right = helper(i + 1, end)
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        all_trees.append(root)
            return all_trees

        return helper(1, n) if n else []