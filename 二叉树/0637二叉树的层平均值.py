# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        from collections import deque
        queue = deque([root])
        res = []
        while queue:
            n = len(queue)
            tmp = 0
            for i in range(n):
                cur = queue.popleft()
                if cur:
                    tmp += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(tmp / n)
        return res