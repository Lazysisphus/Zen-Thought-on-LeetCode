class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp
        # dp[i][j]表示从i开始到j结束的闭区间是否是回文串
        # 如果是回文串，dp[i][j] == True，反之为False
        if not s:
            return 0
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        ans = n
        for i in range(n):
            dp[i][i] = True
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i == 1:
                        dp[i][j] = True # 解决『hh』这种情况
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False
                if dp[i][j]:
                    ans += 1
        return ans