# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.ans = 0
        if not root:
            return 0

        def dfs(node):
            # 1 表示当前结点安装了监控
            # 2 表示当前结点没有监控，但是在监控范围
            # 3 表示当前结点监控不到
            if not node:
                return 2
            left = dfs(node.left)
            right = dfs(node.right)
            if left == 3 or right == 3:
                self.ans += 1
                return 1
            elif left == 1 or right == 1:
                return 2
            else:
                return 3
        
        if dfs(root) == 3:
            self.ans += 1
        return self.ans