# 起床太早了，困啊 ヽ(｀⌒´メ)ノ
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.res = []

    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        # 需要明确能否改变链表的指针方向
        # 方法1：反转链表，时间复杂度O(n)
        if not head:
            return []
        if not head.next:
            return [head.val]
            
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        
        res = []
        while pre:
            res.append(pre.val)
            pre = pre.next
        return res

        # 方法2：使用栈
        # 时间和空间复杂度都是O(n)
        if not head:
            return []

        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res[::-1]

        # 方法3：使用递归
        if not head:
            return []
        else:
            return self.reversePrint(head.next) + [head.val]