# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 时间复杂度O(n)，空间复杂度O(n)
        if not root:
            return []
        from collections import deque
        queue = deque([root])
        ans = []
        while queue:
            tmp = []
            tmp_size = len(queue)
            for i in range(tmp_size):
                cur_node = queue.popleft()
                tmp.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            ans.append(tmp)
        return ans