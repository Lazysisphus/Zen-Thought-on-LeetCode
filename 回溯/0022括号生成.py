'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例：

输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(left, right, tmp):
            if not left and not right:
                res.append(tmp)
            if left:
                backtrack(left - 1, right, tmp + "(")
            if right > left:
                backtrack(left, right - 1, tmp + ")")
        
        if not n:
            return []
        res = []
        backtrack(n, n, "")
        return res