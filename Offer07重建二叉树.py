# 可恶，现在操作都是mac模式 (╯▔皿▔)╯
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 采用递归的思想
        # 在每层递归中，找到“当前前序”和“当前中序”两个序列的根节点
        # 然后这个根节点的左子树的根由“当前前序”和“当前中序”两个序列的对应子序列确定
        # 右子树的根同理
        if not preorder or not inorder:
            return None
        
        # 根据前序序列找到根节点
        root = TreeNode(preorder[0])
        # 判断根节点在中序序列中的位置，由i记录
        for i, num in enumerate(inorder):
            if root.val == num:
                break

        root.left = self.buildTree(preorder[1: i+1], inorder[: i])
        root.right = self.buildTree(preorder[i+1: ], inorder[i+1: ])

        return root
        