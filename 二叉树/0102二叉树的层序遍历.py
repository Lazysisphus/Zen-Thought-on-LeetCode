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
        # 广度优先搜索
        if not root: 
            return [] # 特殊情况，root为空直接返回
        from collections import deque
        # BFS模板内容，BFS关键在于队列的使用
        queue = deque()
        queue.append(root) # 压入初始节点
        res = []
        while queue:
            level = [] # 临时变量，记录当前层的节点
            size = len(queue)
            for _ in range(size): # 遍历某一层的节点
                node = queue.popleft() # 将要处理的节点弹出
                level.append(node.val)
                if node.left: # 如果当前节点有左右节点，则压入队列，根据题意注意压入顺序，先左后右，
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level) # 某一层的节点都处理完之后，将当前层的结果压入结果集
        return res