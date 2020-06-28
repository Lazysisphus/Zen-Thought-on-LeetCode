# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 队列+层次遍历（对应『图』中的宽度优先遍历）
        # 关键点：使用for循环将队列中保存的当前层结点清空
        # 存疑：len(queue)获取queue的长度后，在循环中
        # 向queue添加元素不会影响len(queue)的值
        if not root:
            return []
        
        from collections import deque
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            tmp = []
            for i in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res