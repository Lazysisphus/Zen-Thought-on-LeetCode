class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 双指针 - 滑动窗口
        # 时间复杂度O(n)，空间复杂度O(|s|+|t|)
        need = {} # 统计t中每个字符的出现次数
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        
        window = {}
        flag = 0
        left, right = 0, 0 # 双指针遍历，区间左闭右开
        n = len(s)
        ans = n + 1
        start = 0 # 记录最小覆盖子串的开始位置
        while right < n:
            tmp = s[right] # 当前要滑入窗口的字符
            right += 1
            if tmp in need: # 需要判断加入的字符是否在t中出现
                window[tmp] = window.get(tmp, 0) + 1
                if window[tmp] == need[tmp]:
                    flag += 1
            while flag == len(need): # 只要子串包含t，那么一直循环
                if right - left < ans:
                    ans = right - left
                    start = left # 更新子串的开始位置，最后返回时候要用
                tmp = s[left]
                left += 1
                if tmp in need:
                    if window[tmp] == need[tmp]:
                        flag -= 1
                    window[tmp] -= 1
        return s[start: start + ans] if ans < n + 1 else ""  