class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 确定性有限状态自动机，妙啊
        # 时间复杂度O(n)
        # 参考题解区“JustYou”大佬的答案
        if not s:
            return False

        transTable = [
            [1,2,7,-1,-1,0],
            [-1,2,7,-1,-1,-1],
            [-1,2,3,4,-1,9],
            [-1,3,-1,4,-1,9],
            [6,5,-1,-1,-1,-1],
            [-1,5,-1,-1,-1,9],
            [-1,5,-1,-1,-1,-1],
            [-1,8,-1,-1,-1,-1],
            [-1,8,-1,4,-1,9],
            [-1,-1,-1,-1,-1,9]
        ]

        cols = {
            "sign":0,
            "number":1,
            ".":2,
            "exp":3,
            "other":4,
            "blank":5  
        }

        def get_col(c):
            if c.isdigit():
                return 'number'
            elif c in {'+', '-'}:
                return 'sign'
            elif c == '.':
                return '.'
            elif c in {'E', 'e'}:
                return 'exp'
            elif c == ' ':
                return 'blank'
            else:
                return 'other'

        legal_state = {2, 3, 5, 8, 9}
        state = 0
        for c in s:
            state = transTable[state][cols[get_col(c)]]
            if state == -1:
                return False
        return True if state in legal_state else False