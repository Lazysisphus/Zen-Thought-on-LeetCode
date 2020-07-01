class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # 方法1：动态规划
        # dp[i][j]表示以A[i-1]与B[j-1]结尾的公共字串的长度
        # 时间复杂度O(M*N)，空间复杂度O(M*N)
        rows = len(A) 
        cols = len(B) 
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)] 
        for i in range(1, rows+1): 
            for j in range(1, cols+1): 
                if A[i-1] == B[j-1]: 
                    dp[i][j] = dp[i-1][j-1] + 1 
        return max(max(row) for row in dp)

        # 方法2：滑动窗口
        # 时间复杂度O((M+N)*min(M, N))，空间复杂度O(1)
        def maxLength(addA, addB, length):
            ret = k = 0
            for i in range(length):
                if A[addA + i] == B[addB + i]:
                    k += 1
                    ret = max(ret, k)
                else:
                    k = 0
            return ret
        
        n, m = len(A), len(B)
        ret = 0
        for i in range(n):
            length = min(n-i, m)
            ret = max(ret, maxLength(i, 0, length))
        for i in range(m):
            length = min(n, m-i)
            ret = max(ret, maxLength(0, i, length))
        return ret