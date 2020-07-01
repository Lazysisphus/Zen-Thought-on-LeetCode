# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 其实需要做详细的讨论
        # 如果两个链表有交点，且两链表长度相同，那么在第一次遍历的时候就会找到交点，退出循环
        # 如果两个链表有交点，但是链表长度不同，那么会在第二次交叉遍历的时候在交点相交
        # 如果两个链表没有交点，不管两个链表的长度如何，最后都会有pa==pb==None
        # 时间复杂度O(n)
        if not headA or not headB:
            return None
        
        pa = headA
        pb = headB
        while pa != pb:
            if pa:
                pa = pa.next
            else:
                pa = headB
            if pb:
                pb = pb.next
            else:
                pb = headA
        return pa