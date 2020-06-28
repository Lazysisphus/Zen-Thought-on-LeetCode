# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        # 递归
        # 设A有M个结点，B有N个结点
        def recur(A, B):
            if not B: # 如果B为空，即在B上的遍历越过了叶子结点，说明匹配成功
                return True
            if not A or A.val != B.val: # 如果A为空，说明越过了A的叶子结点，匹配失败
                return False
            flag = recur(A.left, B.left) and recur(A.right, B.right)
            return flag
        
        flag = bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))
        return flag