class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 了解python二进制数的特性
        #   1.python数字以补码形式存储，如果小于0x7fffffff，说明是整数，返回原值，否则是负数
        #   2.python通过某种机制实现了无限长数字的二进制表示，为了获取数字的32位二进制表示，
        #     需要『& 0xffffffff』做截断
        #   3.对于计算得到的32位表示的负数，需要对高位全部取饭以获取python形式的负数表示，即操作~(a^base)
        # 时间复杂度O(1)，空间复杂度O(1)
        base = 0xffffffff
        a, b = a & base, b & base
        while b != 0:
            tmp = a
            a = (a ^ b) & base
            b = (tmp & b) << 1 & base
        return a if a <= 0x7fffffff else ~(a ^ base)