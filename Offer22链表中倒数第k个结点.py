# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 方法1：快慢指针
        # 时间复杂度O(n)，空间复杂度O(1)
        # 注意三个地方：
        #   链表的头结点为空；
        #   链表的长度小于k
        #   k为0或负值
        p1, p2 = head, head
        while k-1:
            p1 = p1.next
            k -= 1
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        return p2