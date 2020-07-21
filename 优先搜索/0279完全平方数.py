class Solution:
    def numSquares(self, n: int) -> int:
        # 整体看作一个在树上遍历的过程
        # 最初，根结点的值是n，根节点的每个子结点，依次是根结点减去1^2、2^2...之后的结果
        # 当遍历到某个结点的值为0时，遍历结束
        # 当遍历到出现过的某值时，跳过，因为之前该值出现时没有得到答案，之后也不会
        from collections import deque
        if n == 0:
            return 0
        
        visited = set()
        queue = deque([[n, 0]])
        while queue:
            for _ in range(len(queue)):
                val, step = queue.popleft()
                for i in range(int(val**0.5), -1, -1): # 这里反向遍历可以减少程序运行时间
                    tmp = val - i**2
                    if tmp == 0:
                        return step+1
                    if not tmp in visited:
                        visited.add(tmp)
                        queue.append([tmp, step+1])