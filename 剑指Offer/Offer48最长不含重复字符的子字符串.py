class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 动态规划
        # 时间复杂度O(n)，空间复杂度O(1)（使用的哈希表长度不会超过26）
        hash_map = {}
        ans = 0
        dpi = 0
        for i in range(len(s)):
            # 得到当前字符上次出现的位置，若该字符不存在字典中，说明字符第一次出现，那么上次位置默认取-1
            j = hash_map.get(s[i], -1)
            hash_map[s[i]] = i # 更新当前字符在哈希表中的位置记录
            # 如果当前字符在以上个字符为结尾的最大无重复字符子串中出现过，那么更新dpi为重复字符中间的距离
            # 否则，更新dpi+1
            dpi = dpi + 1 if (i - j) > dpi else i - j
            ans = max(ans, dpi)
        return ans