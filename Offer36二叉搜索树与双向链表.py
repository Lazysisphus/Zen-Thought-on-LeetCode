"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    # 解释参考题解区K姓大佬
    # 时间复杂度O(n)
    # 空间复杂度O(n)
    def __init__(self):
        self.head = None # 记录链表的头结点
        self.pre = None # 记录当前结点cur的前一个结点

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(cur):
            if not cur: # 如果cur不存在，说明越过了叶结点，返回
                return 
            helper(cur.left) # 递归左子树
            # 处理当前结点
            if not self.pre: # 如果pre为空，进行初始化，记录头结点，头结点指针固定
                self.head = cur
            else: # 如果pre不空，令pre和cur指向对方
                self.pre.right, cur.left = cur, self.pre
            self.pre = cur # 保存cur
            helper(cur.right) # 递归右子树

        if not root:
            return
        helper(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head