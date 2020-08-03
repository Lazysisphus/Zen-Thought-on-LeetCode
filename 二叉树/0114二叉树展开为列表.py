# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 递归
        # 时间复杂度O(n)，空间复杂度O(n)
        if not root or (not root.left and not root.right):
            return root
        # 先把左右子树捋直
        self.flatten(root.left)
        self.flatten(root.right)
        tmp = root.right # 把捋直的右子树备份一下
        root.right = root.left # 把捋直的左子树放到右边
        root.left = None # 记得把左子树置空
        while(root.right): # 找到现在右子树的最后一个node
            root = root.right
        root.right = tmp # 把捋直的原来的右子树接上去

        # 寻找前驱结点
        # 当前结点的右子树根结点的前驱结点是当前结点左子树中最右面的结点
        # 同时，当前结点是其左子树根节点的前驱结点
        cur = root
        while cur:
            if cur.left:
                pre = nxt = cur.left
                while pre.right:
                    pre = pre.right
                pre.right = cur.right
                cur.left = None
                cur.right = nxt
            cur = cur.right