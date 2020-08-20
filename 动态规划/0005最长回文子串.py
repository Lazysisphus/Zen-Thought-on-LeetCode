class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 动态规划，类似题目647
        # 时间复杂度O(n^2)，空间复杂度O(n^2)
        n = len(s)
        if n == 0 or n == 1:
            return s
        
        max_len = 0
        beg, end = 0, 0
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                if dp[i][j] == True and j - i + 1 > max_len:
                    max_len = j - i + 1
                    beg, end = i, j
        return s[beg: end + 1]