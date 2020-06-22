class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        # BFS：使用队列实现
        visited = set()
        queue = collections.deque()
        queue.append((0, 0))
        while queue:
            x, y = queue.popleft()
            if (x, y) not in visited and self.get_sum(x, y) <= k:
                visited.add((x, y))
                for dx, dy in [(1, 0), (0, 1)]: # 只考虑向右和向下两个方向即可
                    if 0<=x+dx<m and 0<=y+dy<n:
                        queue.append((x+dx, y+dy))
        return len(visited)

        # DFS
        def dfs(i, j):
            if i == m or j == n or self.get_sum(i, j) > k or (i, j) in visited:
                return 
            visited.add((i, j))
            dfs(i+1, j)
            dfs(i, j+1)
            
        visited = set()
        dfs(0, 0)
        return len(visited)

    def get_sum(self, row, col):
        tmp = 0
        while row:
            tmp = tmp + row%10
            row = row // 10
        while col:
            tmp = tmp + col%10
            col = col // 10
        return tmp