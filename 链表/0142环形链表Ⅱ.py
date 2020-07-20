# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 如果链表为空，或者头结点无后继结点
        if not head or not head.next:
            return None
        
        flag = False
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                flag = True
                break
        
        if not flag:
            return None
        else:
            count = 1
            begin = slow
            end = slow.next
            while end != begin:
                end = end.next
                count += 1

            slow = head
            fast = head
            for i in range(count):
                fast = fast.next
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return slow