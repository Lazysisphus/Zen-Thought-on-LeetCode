"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        # step1
        cur = head
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next

        # step2
        cur = head
        while cur:
            tmp = cur.next
            if not cur.random:
                tmp.random = None
            else:
                tmp.random = cur.random.next
            cur = tmp.next
        
        # step3
        cur = head
        copyed_head = head.next
        while cur:
            tmp = cur.next
            cur.next = tmp.next
            if tmp.next:
                tmp.next = tmp.next.next
            cur = cur.next
        return copyed_head