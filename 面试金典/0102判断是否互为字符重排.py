"""
面试题 01.02. 判定是否互为字符重排
给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

示例 1：

输入: s1 = "abc", s2 = "bca"
输出: true 
示例 2：

输入: s1 = "abc", s2 = "bad"
输出: false
说明：

0 <= len(s1) <= 100
0 <= len(s2) <= 100
"""

class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        # 使用字典，空间复杂度O(n)，时间复杂度O(n)
        if len(s1) != len(s2):
            return False
        
        hash_map = {}
        for ch in s1:
            hash_map[ch] = hash_map.get(ch, 0) + 1
        for ch in s2:
            hash_map[ch] = hash_map.get(ch, 0) - 1
        for k in hash_map:
            if hash_map[k] != 0:
                return False
        return True

        # 使用排序，空间复杂度O(1)，时间复杂度O(nlogn)
        return sorted(s1) == sorted(s2)