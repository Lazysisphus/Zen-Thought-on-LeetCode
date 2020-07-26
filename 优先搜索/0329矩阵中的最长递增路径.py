class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # 使用带记忆的dfs
        # 路径可以从任意一个单元格开始，向其四个方向蔓延，因此
        # 需要以矩阵的每一个单元格为出发点，进行深度优先搜索
        def dfs(x, y):
            if memory[x][y] != 0:
                return memory[x][y]
            res = 1 # 记录以(x, y)为出发点的最长单调路径长度
            for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < row and 0 <= ny < col and matrix[nx][ny] > matrix[x][y]:
                    res = max(res, dfs(nx, ny) + 1) # 更新res为四个方向上最长路径的长度，递归体现在这里
            memory[x][y] = max(res, memory[x][y]) # 更新memory[x][y]值为从(x, y)出发的最长路径长度
            return memory[x][y]

        if not matrix or not matrix[0]:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        memory = [[0 for _ in range(col)] for _ in range(row)]
        return max(dfs(i, j) for i in range(row) for j in range(col))