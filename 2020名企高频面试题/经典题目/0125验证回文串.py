class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 使用python字符串翻转
        # 时间复杂度O(n)，空间复杂度O(n)
        ans = ""
        for ch in s:
            if ch.isalnum():
                ans = ans + ch.lower()
        return ans == ans[::-1]

        # 双指针
        # 时间复杂度O(n)，空间复杂度O(1)
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
        return True