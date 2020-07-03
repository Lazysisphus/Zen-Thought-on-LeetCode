"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # 原地复制链表
        # 时间复杂度O(n)，空间复杂度O(1)
        if not head:
            return head
        
        cur = head
        while cur:
            temp = Node(cur.val)
            temp.next = cur.next
            cur.next = temp
            cur = temp.next
        
        cur = head
        while cur:
            temp = cur.next
            if cur.random:
                temp.random = cur.random.next
            cur = temp.next
        
        raw = head
        new = head.next
        while raw:
            temp = raw.next
            raw.next = temp.next
            if temp.next:
                temp.next = temp.next.next
            # 每次循环结束，把raw的位置更新好就可以了，temp的位置在循环开始的地方会根据raw进行更新
            raw = raw.next
        return new