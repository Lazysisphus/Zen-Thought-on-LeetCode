# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 这道题和链表是否有序好像没什么关系 = =
        if not head or not head.next:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next
        return dummy.next