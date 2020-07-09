class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 动态规划
        # 设字符串为X1X2...X(i-2)X(i-1)Xi...Xn-1Xn，设以Xi结尾的翻译方法有dp[i]种
        # 以Xi结尾的翻译方法：即翻译结果必须包含对Xi的翻译
        # 状态转移：如果X(i-1)Xi构成的数字在合法范围([10, 25])，那么dp[i]=dp[i-1]+dp[i-2]
        #          否则dp[i]=dp[i-1]
        # 时间复杂度O(n)，空间复杂度O(n)
        s = str(num)
        a, b = 1, 1 # 初始化dp[1]与dp[0]，dp[0]=1是因为dp[0]+dp[1]=dp[2]=2
        for i in range(2, len(s)+1):
            a, b = (a + b if '10' <= s[i-2: i] <= '25' else a), a
        return a # 返回dp[n-1]，dp[n]=dp[n-1]

        # 进一步改进空间复杂度为O(1)
        # 从个位开始不断获得最低的两位数字y和x
        # %表示获得最低位数字，//表示将原数字的最低位删除
        a = b = 1
        y = num % 10
        while num != 0:
            num //= 10
            x = num % 10
            a, b = (a + b if 10 <= 10 * x + y <= 25 else a), a
            y = x
        return a