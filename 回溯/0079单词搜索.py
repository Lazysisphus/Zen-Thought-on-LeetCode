'''
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "A
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, word):
            if len(word) == 0:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
                return False
            tmp = board[i][j]
            board[i][j] = 0
            flag = dfs(i + 1, j, word[1: ]) or dfs(i - 1, j, word[1: ]) or dfs(i, j + 1, word[1: ]) or dfs(i, j - 1, word[1: ])
            board[i][j] = tmp
            return flag
        
        if not board or not board[0]:
            return False
        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, word):
                    return True
        return False