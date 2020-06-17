class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 方法1：使用额外空间存储新字符串
        # 时间和空间复杂度都是O(n)
        res = ''
        for ch in s:
            if ch == ' ':
                res += '%20'
            else:
                res += ch
        return res

        # 方法2：使用两个指针从后向前遍历s
        # 一个指针指向s中当前需要判断值的字符
        # 另一个指针指向新字符串的末尾
        # 当两个指针相遇，遍历结束
        # 时间复杂度O(n)，空间复杂度O(1)
        # 在C中比较直观好实现，python直接用replace吧
        return s.replace(" ", "%20");
