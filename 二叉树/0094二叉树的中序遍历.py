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
        res = []
        stack = []
        while stack or root:
			# 不断往左子树方向走，每走一次就将当前节点保存到栈中
			# 这是模拟递归的调用
			while root:
				stack.append(root)
				root = root.left
			# 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
			# 然后转向右边节点，继续上面整个过程
            tmp = stack.pop()
            res.append(tmp.val)
            root = tmp.right
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
