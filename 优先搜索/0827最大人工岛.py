class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # 和拼多多笔试题很像
        # https://blog.csdn.net/alexandsunny/article/details/108355698
        def dfs(i, j, grid, numorder):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            if grid[i][j] != 1:
                return 0
            grid[i][j] = numorder
            return 1 + dfs(i - 1, j, grid, numorder) + dfs(i + 1, j, grid, numorder) \
                     + dfs(i, j - 1, grid, numorder) + dfs(i, j + 1, grid, numorder)

        index = 2
        land = {}
        totalareas = 0
        maxland = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    land[index] = dfs(i, j, grid, index)
                    totalareas += land[index]
                    maxland = max(maxland, land[index])
                    index += 1
        maxarea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    tmp = set()
                    tmpsum = 0
                    if i > 0:   tmp.add(grid[i - 1][j])
                    if i < len(grid) - 1:   tmp.add(grid[i + 1][j])
                    if j > 0:   tmp.add(grid[i][j - 1])
                    if j < len(grid[0]) - 1:    tmp.add(grid[i][j + 1])
                    tmp = list(tmp)
                    for k in range(len(tmp)):
                        tmpsum += land.get(tmp[k], 0)
                    maxarea = max(maxarea, tmpsum)
        maxarea = max(maxland, maxarea)
        return min(maxarea + 1, len(grid) * len(grid[0]))