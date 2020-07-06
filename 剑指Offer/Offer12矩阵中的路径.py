class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 回溯+DFS
        def dfs(board, i, j, word):
            if len(word) == 0:
                return True
            if i<0 or i>len(board)-1 or j<0 or j>len(board[0])-1 or board[i][j] != word[0]:
                return False
            tmp = board[i][j]
            board[i][j] = 0
            flag = dfs(board, i-1, j, word[1:]) or dfs(board, i+1, j, word[1:]) or dfs(board, i, j-1, word[1:]) or dfs(board, i, j+1, word[1:])
            board[i][j] = tmp
            return flag

        if len(word) == 0:
            return True
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if dfs(board, i, j, word):
                    return True
        return False