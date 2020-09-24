# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        res = []
        pre_val = None
        cnt = 0
        max_cnt = 0

        def inorder(node):
            nonlocal res, pre_val, cnt, max_cnt
            if not node:
                return
            inorder(node.left)
            if node.val == pre_val:
                cnt += 1
            else:
                cnt = 1
                pre_val = node.val
            if cnt == max_cnt:
                res.append(node.val)
            elif cnt > max_cnt:
                res = [node.val]
                max_cnt = cnt
            inorder(node.right)
        
        inorder(root)
        return res