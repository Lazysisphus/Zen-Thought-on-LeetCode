class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 『0000』到『9999』共有一万个状态，可以看做一万个结点
        # 每个结点有4位，每位可进行『+1』和『-1』两种变换
        # 因此，每个结点最多有8个相邻的结点，这里『最多』是因为结点的邻结点可能是『死结点』
        # 从『0000』开始搜索，直到找到目标结点，或者目标结点不可到达，结束BFS
        from collections import deque
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        
        queue = deque([["0000", 0]]) # status, step
        while len(queue):
            node, step = queue.popleft()
            for pos in range(4):
                for change in [-1, +1]:
                    new_node = node[: pos] + str((int(node[pos])+change) % 10) + node[pos+1: ]
                    if new_node == target:
                        return step + 1
                    if not new_node in deadends:
                        queue.append([new_node, step+1])
                        deadends.add(new_node)
        return -1