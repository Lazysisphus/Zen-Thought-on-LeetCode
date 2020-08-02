# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        # 前序：根-左-右
        # 后序：左-右-根
        # 找个例子分析，关键是找到左右子树的分界线
        if not pre:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        root = TreeNode(pre[0])
        pos = 0
        while post[pos] != pre[1]:
            pos += 1
        root.left = self.constructFromPrePost(pre[1: 2 + pos], post[: 1 + pos])
        root.right = self.constructFromPrePost(pre[2 + pos: ], post[1 + pos: -1])
        return root