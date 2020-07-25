"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 队列，层级遍历
        if not root:
            return root
        from collections import deque
        queue = deque([root])
        while queue:
            n = len(queue) # 这里一定要先获取长度，记录下来！！！
            for i in range(n):
                cur = queue.popleft()
                if i < n - 1:
                    cur.next = queue[0]
                if cur.left:
                    queue.append(cur.left) 
                if cur.right:
                    queue.append(cur.right)
        return root