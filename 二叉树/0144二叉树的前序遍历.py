# 爷，带薪做题，提升自己 (*ﾟ∀ﾟ*)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 方法1：递归实现
        def helper(root):
            if not root:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        res = []
        helper(root)
        return res

        # 方法2：循环实现
        # 程序直观不好理解，画一棵树举例想想
        #     10
        #    /   \
        #   6    14
        #  / \   / \
        # 4   8 12 16
        if not root:
            return []
        cur, res, stack = root, [], []
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            tmp = stack.pop()
            cur = tmp.right
        return res

        # 方法3：颜色标记法，实质还是栈
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: 
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
                stack.append((GRAY, node))
            else:
                res.append(node.val)
        return res