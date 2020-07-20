class Solution(object):
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        # python的 and 操作如果最后结果为真，返回最后一个表达式的值，
        # or 操作如果结果为真，返回第一个结果为真的表达式的值
        # 时间复杂度O(n)，空间复杂度O(n)
        return n and (n + self.sumNums(n-1))