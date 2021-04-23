"""
面试题 01.05. 一次编辑
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

 

示例 1:

输入: 
first = "pale"
second = "ple"
输出: True
 

示例 2:

输入: 
first = "pales"
second = "pal"
输出: False

参考题解：
https://leetcode-cn.com/problems/one-away-lcci/solution/mian-shi-ti-0105-yi-ci-bian-ji-shuang-zh-5fzv/
"""

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        # 双指针法，时间复杂度O(len1+len2)，空间复杂度O(1)
        len1, len2 = len(first), len(second)
        if abs(len1 - len2) > 1:
            return False
        
        cnt = 0
        i, j = 0, 0
        while i < len1 and j < len2:
            if first[i] == second[j]:
                i += 1
                j += 1
                continue # 如果两个指针当前指向的字符相同，一直向后遍历
            # 如果两个指针当前指向的字符串不同，两指针向后移动1位，同时记录一次编辑
            i += 1
            j += 1
            cnt += 1
            if cnt > 1:
                return False
            if len1 != len2: # 两个字符串长度不一致，只能通过删除或者插入来编辑
                if len1 < len2:
                    i -= 1
                else:
                    j -= 1
        return True