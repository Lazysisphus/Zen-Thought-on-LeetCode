# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 使用快慢指针搜索链表的中间结点
        # 找到后，慢指针指向中间结点，pre指向中间结点的前一个结点
        # 随后将链表断开，使用递归结构构造二叉搜索树
        # 注意两种返回情况：
        #   如果当前头结点为空，返回
        #   如果当前链表只包含一个结点，那么返回该结点
        if not head:
            return

        pre, slow, fast = head, head, head
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        root = TreeNode(slow.val)
        if fast == slow:
            return root
        
        pre.next = None
        r_head = slow.next
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(r_head)
        return root