"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        from collections import deque
        seen = {} # 使用哈希表记录克隆过的结点，并将原图结点与其克隆结点对应
        # dfs
        # 时间复杂度O(n)，空间复杂度O(n)
        def dfs(node):
            if not node:
                return 
            if node in seen:
                return seen[node]
            clone = Node(node.val, [])
            seen[node] = clone
            for nei in node.neighbors:
                seen[node].neighbors.append(dfs(nei))
            return clone
        
        # bfs
        # 时间复杂度O(n)，空间复杂度O(n)
        def bfs(node):
            if not node:
                return
            clone = Node(node.val, [])
            seen[node] = clone
            queue = deque([node])
            while queue:
                tmp = queue.pop()
                for nei in tmp.neighbors:
                    if nei not in seen:
                        seen[nei] = Node(nei.val, []) # 加入哈希表
                        queue.append(nei) # 加入队列
                    seen[tmp].neighbors.append(seen[nei])
            return clone

        # return dfs(node)
        return bfs(node)