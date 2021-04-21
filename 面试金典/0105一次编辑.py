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
"""

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
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
            i += 1
            j += 1
            cnt += 1 # 累计一次编辑 
            if cnt > 1:
                return False
            if len1 != len2:
                if len1 < len2:
                    i -= 1
                else:
                    j -= 1
        return True