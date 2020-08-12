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
                grid[i][j] = "0"
                x, y = queue.popleft()
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    if 0 <= x+dx < row and 0 <= y+dy < col and grid[x+dx][y+dy] == "1":
                        grid[x+dx][y+dy] = "0"
                        queue.append([x+dx, y+dy])
        # 深度优先搜索
        def dfs(i, j):
            grid[i][j] = "0"
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                new_i = i + dx
                new_j = j + dy
                if 0 <= new_i < row and 0 <= new_j < col and grid[new_i][new_j] == "1":
                    dfs(new_i, new_j)

        from collections import deque
        if not grid or not grid[0]:
            return 0
        cnt = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                # 发现一个岛屿，计数并开始遍历
                if grid[i][j] == "1":
                    cnt += 1
                    bfs(i, j)
                    # dfs(i, j)
        return cnt