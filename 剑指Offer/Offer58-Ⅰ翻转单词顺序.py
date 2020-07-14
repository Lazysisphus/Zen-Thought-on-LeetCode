class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 方法1：
        # split()：如果 sep 未指定或为 None，则会应用另一种
        # 拆分算法：连续的空格会被视为单个分隔符，其结果将不包含
        # 开头或末尾的空字符串，如果字符串包含前缀或后缀空格的话
        # 时间复杂度O(n)
        if not s:
            return ""
        return " ".join(s.split()[::-1])

        # 方法2：滑动窗口
        # 时间复杂度O(n)
        if not s:
            return ""
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != " ":
                i -= 1
            res.append(s[i+1: j+1])
            while s[i] == ' ': 
                i -= 1 # 跳过单词间空格
            j = i # j 指向下个单词的尾字符
        return ' '.join(res)