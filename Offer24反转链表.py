# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 方法1：循环
        if not head or not head.next:
            return head
        
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

        # 方法2：递归，不好理解啊
        if not head or not head.next:
            return head
        
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node