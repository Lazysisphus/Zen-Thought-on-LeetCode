"""
面试题 01.04. 回文排列
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

回文串不一定是字典当中的单词。

 

示例1：

输入："tactcoa"
输出：true（排列有"tacocat"、"atcocta"，等等）
"""

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # 采用位运算，时间复杂度O(n)，空间复杂度O(1)
        memory = 0
        for ch in s:
            memory = memory ^ (1 << ord(ch))
        if memory & (memory - 1) == 0: # 判断一个数是否为2的整数次
            return True
        else:
            return False