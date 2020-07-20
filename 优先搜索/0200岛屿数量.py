class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 宽度优先搜索
        def bfs(i, j):
            queue = deque([[i, j]])
            while len(queue):
                x, y = queue.popleft()
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    if 0 <= x+dx < row and 0 <= y+dy < col and grid[x+dx][y+dy] == "1":
                        grid[x+dx][y+dy] = "0"
                        queue.append([x+dx, y+dy])

        from collections import deque
        if not grid or not grid[0]:
            return 0
        cnt = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                # 发现一个岛屿，计数、置零、入队
                if grid[i][j] == "1":
                    cnt += 1
                    grid[i][j] = "0"
                    bfs(i, j)
        return cnt