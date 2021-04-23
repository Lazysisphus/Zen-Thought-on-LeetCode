"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
 

限制：

0 <= 链表长度 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


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
        # 方法1
        # 反转链表，时间复杂度O(n)
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

        # 方法2
        # 使用栈，时间和空间复杂度都是O(n)
        if not head:
            return []

        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res[::-1]

        # 方法3
        # 使用递归
        if not head:
            return []
        else:
            return self.reversePrint(head.next) + [head.val]