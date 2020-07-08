class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 找规律题目真的需要一点耐心
        # 时间复杂度O(logn)，空间复杂度O(1)
        digit, start, count = 1, 1, 9 # 这里从数字1开始计数，数字1是第1位
        # 首先找到目标位所在的数字是几位数
        while n > count:
            n -= count
            digit += 1
            start *= 10
            count = digit * start * 9
        # 其次找到目标位所在的数字num
        num = start + (n-1) // digit
        # 最后找到目标位在num的第几位，从而得到答案
        ans = str(num)[(n-1)%digit]
        return int(ans)