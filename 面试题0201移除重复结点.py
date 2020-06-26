# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeDuplicateNodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 方法1：使用临时缓存区
        # 时间复杂度O(n)，空间复杂度O(n)
        if not head or not head.next:
            return head

        hash_map = {}
        hash_map[head.val] = 1
        cur = head
        while cur.next:
            hash_map[cur.next.val] = hash_map.get(cur.next.val, 0) + 1
            if hash_map[cur.next.val] == 1:
                cur = cur.next
            else:
                cur.next = cur.next.next
        return head

        # 方法2：两层循环，暴力解法
        # 时间复杂度O(n^2)，空间复杂度O(1)
        # python会超时
        if not head or not head.next:
            return head
    
        out_p = head
        del_p = head # 在内循环中，删除del_p的下一个元素
        while out_p:
            while del_p.next:
                if del_p.next.val == out_p.val:
                    del_p.next = del_p.next.next
                else:
                    del_p = del_p.next
            out_p = out_p.next
            del_p = out_p
        return head