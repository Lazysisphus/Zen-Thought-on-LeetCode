# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 方法1：递归遍历
        res = []
        def helper(root):
            if not root:
                return 
            helper(root.left)
            helper(root.right)
            res.append(root.val)
        helper(root)

        return res

        # 方法2：循环实现
        res = []
        stack = []  
        node = root
        while stack or node:
            while node:
                stack.append(node) # 第一次入栈的是根节点
                # 判断当前节点的左子树是否存在，若存在则持续左下行，若不存在就转向右子树
                node = node.left if node.left is not None else node.right
            # 循环结束说明走到了叶子节点，没有左右子树了，该叶子节点即为当前栈顶元素，应该访问了
            node = stack.pop() # 取出栈顶元素进行访问
            res.append(node.val) # 将栈顶元素也即当前节点的值添加进res
            # 下面的stack[-1]是执行完上面那句取出栈顶元素后的栈顶元素
            if stack and stack[-1].left == node: # 若栈不为空且当前节点是栈顶元素的左节点
                node = stack[-1].right # 则转向遍历右节点
            else:
                node = None # 没有左子树或右子树，强迫退栈
                
        return res

        # 方法3：颜色标记法
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == WHITE:
                stack.append((GRAY, node))
                stack.append((WHITE, node.right))
                stack.append((WHITE, node.left))
            elif color == GRAY:
                res.append(node.val)
        
        return res
