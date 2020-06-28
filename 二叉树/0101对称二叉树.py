# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 方法1：递归
        def check(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return check(node1.left, node2.right) and check(node1.right, node2.left)
        return check(root, root)

        # 方法2：层序遍历，判断每层是否回文
        if not root: 
            return True

        queue = [root]
        while queue:
            cur_layer = []
            next_layer = []
            for node in queue:
                if not node:
                    cur_layer.append(None)
                    continue
                next_layer.append(node.left)
                next_layer.append(node.right)
                cur_layer.append(node.val)
            if cur_layer != cur_layer[::-1]:
                return False
            queue = next_layer
        return True