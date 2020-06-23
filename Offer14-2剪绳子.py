class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 和上题相似，不过结果可能的范围变大了
        # 直接使用贪心来解
        if n == 2:
            return 1
        if n == 3:
            return 2
        
        times_of_3 = n // 3
        if n - times_of_3 * 3 == 1:
            times_of_3 -= 1
        times_of_2 = (n - (times_of_3 * 3)) // 2
        res = pow(3, times_of_3) * pow(2, times_of_2)
        return res % 1000000007