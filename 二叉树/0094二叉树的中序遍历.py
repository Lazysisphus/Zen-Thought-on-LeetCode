# 写着写着下暴雨了，听一首六月的雨，给我自己
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 方法1：递归
        res = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        return res

        # 方法2：迭代
        if not root:
            return res
        cur, res, stack = root, [], []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            tmp = stack.pop()
            res.append(tmp.val) # 和前序不同，添加结点的位置要靠后
            cur = tmp.right
        return res

        # 方法3：颜色标记法
        res = []
        WHITE, GRAY = 0, 1
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: 
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res