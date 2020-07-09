class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 题解区K大佬的答案真的绝了
        # 时间复杂度O(logn)，空间复杂度O(1)
        digit, res = 1, 0
        high, cur, low = n//10, n%10, 0
        while high != 0 or cur != 0:
            if cur == 0: 
                res += high * digit
            elif cur == 1: 
                res += high * digit + low + 1
            else: 
                res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res