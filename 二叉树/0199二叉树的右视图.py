# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # bfs
        # 时间复杂度O(n)，空间复杂度O(n)
        if not root:
            return []
        from collections import deque
        ans = []
        queue = deque([root])
        while queue:
            cur_size = len(queue)
            for i in range(cur_size):
                node = queue.popleft()
                if i == cur_size - 1:
                    ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans