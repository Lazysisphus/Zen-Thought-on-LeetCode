# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # 二插搜索树的中序遍历，会将树中元素按照从小到大的顺序排序
        # 反向中序遍历，就会将二插搜索树中的元素从大到小排序
        # 那么在反向遍历的过程中，进行累加即可
        # 时间复杂度O(n)，空间复杂度O(n)
        def helper(root):
            nonlocal num
            if not root:
                return root
            helper(root.right)
            root.val += num
            num = root.val
            helper(root.left)
            return root
        
        num = 0
        helper(root)
        return root