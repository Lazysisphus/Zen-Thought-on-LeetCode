class Solution(object):
    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 动态规划，在原始grid上进行修改，优化了空间复杂度
        # 时间复杂度O(mn)，空间复杂度O(1)
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        for j in range(1, n): # 初始化第一行
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m): # 初始化第一列
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]