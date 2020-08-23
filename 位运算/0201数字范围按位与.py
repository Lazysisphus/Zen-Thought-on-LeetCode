class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # 将题目转化为寻找范围内，所有数字二进制形式的最长公共前缀
        # 在最长公共前缀后面补零，即可得到所有数字按位“与”的结果
        # 时间复杂度O(logn)，空间复杂度O(1)
        shift = 0
        while m != n:
            m >>= 1
            n >>= 1
            shift += 1
        m <<= shift
        return m