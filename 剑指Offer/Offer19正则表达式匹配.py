class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # 题解区橘子大佬的解答言简意赅
        # 方法1：递归
        if not p: # 被这里惊艳到，仔细分析的话其实就是简单的逻辑推理，但是code很简练
            return not s
        first_match = bool(s and p[0] in {s[0], '.'}) # 首先判断第一个字符是否匹配
        # 其次判断第二个字符是否匹配
        if len(p) >= 2 and p[1] == "*": # 如果p的第二个字符是*，分情况讨论
            return self.isMatch(s, p[2: ]) or (first_match and self.isMatch(s[1: ], p))
        else: # 如果p的第二个字符不是*，情况比较简单
            return first_match and self.isMatch(s[1: ], p[1: ])

        # 方法2：动态规划
        if not p:
            return not s
        if not s and len(p) == 1: # 这里条件必须是等于1，不能大于1 
            return False

        # 初始状态
        # dp[i][j]，s的前i个字符和p的前j个字符是否匹配
        m, n = len(s)+1, len(p)+1
        dp = [[False for _ in range(n)] for _ in range(m)]
        dp[0][0] = True
        dp[0][1] = False

        # 初始化矩阵的第一行，c即col
        for c in range(2, n):
            j = c - 1 # j取值范围[1, n-2]，即[1, len(p)-1]，也就是p中除了第一个字符都可以取*
            if p[j] == '*':
                dp[0][c] = dp[0][c - 2]
        
        for r in range(1, m):
            i = r - 1
            for c in range(1, n):
                j = c - 1
                if s[i] == p[j] or p[j] == '.':
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[j] == '*':
                    if p[j - 1] == s[i] or p[j - 1] == '.': # ‘*’前面的字符匹配s[i]，或者为'.'
                        dp[r][c] = dp[r - 1][c] or dp[r][c - 2]
                    else: # ‘*’匹配了0次前面的字符
                        dp[r][c] = dp[r][c - 2] 
                else:
                    dp[r][c] = False
        return dp[m - 1][n - 1]