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
        # 注意：这里删除的是内层结点，所以
        if not head or not head.next:
            return head
    
        cur = head
        del_p = head # dep_p是快指针，对应每个cur，del_p扫描整个链表
        while cur:
            while del_p.next:
                if del_p.next.val == cur.val:
                    del_p.next = del_p.next.next
                else:
                    del_p = del_p.next
            cur = cur.next
            del_p = cur
        return head