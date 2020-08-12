class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 思路：边界O及边界联通O是一种类型的O，该类型O不需要用X填充，其余O需要用X填充
        # 因此，先将不需要填充的O用A标记，然后遍历整个矩阵，将A恢复为O，将O填充为X即可
        # 将O标记为A时，使用dfs，从边界开始遍历（第一行、最后一行、第一列、最后一列）
        # 时间复杂度O(mn)，空间复杂度O(mn)
        if not board or not board[0]:
            return board
        row = len(board)
        col = len(board[0])
        if row < 3 or col < 3:
            return board
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= row or j >= col or board[i][j] != "O":
                return
            board[i][j] = "A"
            for nx, ny in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                dfs(nx, ny)

        for i in range(row):
            dfs(i, 0)
            dfs(i, col-1)
        
        for j in range(col):
            dfs(0, j)
            dfs(row-1, j)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'
        return board