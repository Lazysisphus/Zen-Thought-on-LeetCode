# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 前序；根-左-右
        # 中序：左-根-右
        if not inorder: # 如果中序（或者前序）遍历的序列不存在，那么返回空结点
            return None
        root = TreeNode(preorder[0]) # 通过后序序列确定当前的根结点
        pos = 0 # 找到根结点在中序序列中的位置
        while inorder[pos] != root.val:
            pos += 1
        root.left = self.buildTree(preorder[1: 1 + pos], inorder[: pos]) # 递归构造左子树
        root.right = self.buildTree(preorder[1 + pos: ], inorder[pos + 1: ]) # 递归构造右子树
        return root