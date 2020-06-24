# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # 这道题把原题的精髓都改没了
        # 原题给了链表头指针，给了链表中要删除结点的指针
        # 然后要求使用O(1)的时间复杂度删除该指针
        # 删除的时候，需要考虑下述特殊情况：
        # 1-链表为空，或者要删除结点的指针为空
        # 2-链表只有一个结点
        # 3-链表有多个结点，要删除的结点是尾结点

        # 该题通过遍历解决
        # 如果删除头结点
        if head.val == val: 
            return head.next
        pre, cur = head, head.next
        while cur and cur.val != val:
            pre, cur = cur, cur.next
        if cur: 
            pre.next = cur.next
        return head