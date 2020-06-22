class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 本质是计算斐波那契数列，初始值不一样
        a = 1
        b = 2
        for i in range(n-1):
            a, b = b, a+b
        return a % 1000000007
        