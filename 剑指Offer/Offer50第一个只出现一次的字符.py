class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 两次遍历字符串s
        # 第一次统计各个字符出现的次数
        # 第二次寻找第一个只出现一次的字符
        if not s:
            return " "
        hash_map = {}
        for c in s:
            hash_map[c] = hash_map.get(c, 0) + 1
        for c in s:
            if hash_map[c] == 1:
                return c
        return " "