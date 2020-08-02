class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp
        # 时间复杂度O(mn)，空间复杂度O(1)
        if not grid or not grid[0]:
            return 0
        
        row = len(grid)
        col = len(grid[0])
        # 处理第 0 行
        for j in range(1, col):
            grid[0][j] += grid[0][j-1]
        # 处理第 0 列
        for i in range(1, row):
            grid[i][0] += grid[i-1][0]
        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]       