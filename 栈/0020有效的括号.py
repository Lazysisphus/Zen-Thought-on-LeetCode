class Solution:
    def isValid(self, s: str) -> bool:
        # 使用这个程序设计，逻辑要更清晰
        # 时间复杂度O(n)，空间复杂度O(n)
        if not s:
            return True

        stack = []
        pairs = {"}": "{", "]": "[", ")": "("}
        for ch in s:
            if ch in pairs:
                if stack and stack[-1] == pairs[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return not stack