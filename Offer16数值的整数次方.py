class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 方法1：在循环中实现幂乘
        # 注意对幂为负情况的处理
        # 时间复杂度O(n)
        # 在线提交无法通过
        if x == 0 and n < 0: # 底数为0且幂小于0
            return 0

        res = 1
        if n < 0: # 幂小于0
            n = abs(n)
            for i in range(n):
                res *= x
            return 1.0/res
        else: # 幂大于0
            for i in range(n):
                res *= x
            return res

        # 方法2：快速幂方法
        # 题解区大佬就是硬气
        # 时间复杂度O(logn)
        if x == 0: 
            return 0
        res = 1
        if n < 0: 
            x, n = 1/x, -n
        while n:
            if n & 1: 
                res *= x
            x *= x
            n >>= 1
        return res