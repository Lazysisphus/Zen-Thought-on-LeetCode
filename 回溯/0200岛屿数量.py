class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 方法1：宽度优先搜索
        from collections import deque
        if not grid:
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
                    # 宽度优先部分
                    pos_que = deque()
                    pos_que.append([i, j])
                    while len(pos_que)>0:
                        x, y = pos_que.popleft()
                        for new_x, new_y in [[x, y+1], [x+1, y], [x, y-1], [x-1, y]]:
                            if 0<=new_x<row and 0<=new_y<col and grid[new_x][new_y]=="1":
                                grid[new_x][new_y] = "0"
                                pos_que.append([new_x, new_y])
        return cnt
