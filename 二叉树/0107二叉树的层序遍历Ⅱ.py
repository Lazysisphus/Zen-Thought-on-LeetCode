# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # 输出二叉树逆向层序遍历的结果
        if not root:
            return []
        from collections import deque
        queue = deque([root])
        res = []
        while queue:
            n = len(queue)
            tmp = []
            for i in range(n):
                cur = queue.popleft()
                tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(tmp)
        return res[:: -1]