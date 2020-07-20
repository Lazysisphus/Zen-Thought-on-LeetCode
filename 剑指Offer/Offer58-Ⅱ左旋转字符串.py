class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        # 方法1：切片拼接
        # 时间复杂度O(n)，空间复杂度O(n)
        s1 = s[: n]
        s2 = s[n: ]
        s = s2 + s1
        return s

        # 方法2：三次反转
        # 时间复杂度O(n)，空间复杂度O(n)
        s = s[: n][::-1] + s[n: ][::-1]
        s = s[::-1]
        return s