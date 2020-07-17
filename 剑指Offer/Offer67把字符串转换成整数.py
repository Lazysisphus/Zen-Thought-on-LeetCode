class Solution(object):
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        # 方法1：使用正则表达式
        # []中的多个字符会任选一个出现
        # *表示字符出现0次或者多次
        # ？表示字符出现0次或者1次
        # \d表示0~9的数字
        import re
        matches = re.match('[ ]*([+-]?\d+)', str)
        if not matches:
            return 0
        res = int(matches.group(1)) # group()表示返回第一个小括号中的内容
        return 

        # 方法2：基于运算转换
        ls = list(str.strip())
        if not ls: 
            return 0
        flag = -1 if ls[0] == '-' else 1
        if ls[0] in ['+', '-']: del ls[0]
        res, i = 0, 0
        while i < len(ls) and ls[i].isdigit():
            res = res * 10 + ord(ls[i]) - ord('0')
            i += 1
        return min(max(res * flag, -2**31), 2**31-1)