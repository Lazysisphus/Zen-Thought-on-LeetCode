class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 模拟竖式加法
        # 时间复杂度O(max(m, n))，空间复杂度O(1)(?)
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        res = ""
        while i >= 0 or j >= 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            tmp = x + y + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i -= 1
            j -= 1
        return "1" + res if carry else res