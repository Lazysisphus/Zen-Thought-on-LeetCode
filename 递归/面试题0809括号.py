class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def recur(tmp, left, right):
            # 隐含条件，对于合法的括号组合方式，当前剩余的左括号数目
            # 总是小于等于当前剩余的有括号的数目，否则组合非法，需要剪枝
            if left > right:
                return 
            if right == 0:
                res.append(tmp)
            if left > 0:
                recur(tmp+"(", left-1, right)
            if right > 0:
                recur(tmp+")", left, right-1)
        
        recur("", n, n)
        return res