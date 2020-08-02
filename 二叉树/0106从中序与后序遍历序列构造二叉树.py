# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder: # 如果中序（或者后序）遍历的序列不存在，那么返回空结点
            return None
        root = TreeNode(postorder[-1]) # 通过后序序列确定当前的根结点
        pos = 0 # 找到根结点在中序序列中的位置
        while inorder[pos] != root.val:
            pos += 1
        root.left = self.buildTree(inorder[: pos], postorder[: pos]) # 递归构造左子树
        root.right = self.buildTree(inorder[pos + 1: ], postorder[pos: -1]) # 递归构造右子树
        return root