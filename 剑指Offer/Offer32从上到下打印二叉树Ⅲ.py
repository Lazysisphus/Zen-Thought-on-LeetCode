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
        if not root:
            return []
        
        from collections import deque
        queue = deque()
        queue.append(root)
        res = []
        flag = 1 # 1：从左向右，0：从右向左
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if flag == 1:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            flag = 1 - flag
        return res