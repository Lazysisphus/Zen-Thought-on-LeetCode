class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]
        
        # dp[i][j][k]表示在[i,j]部分能得到的最大得分
        # k表示boxes[i]左边有k个与之相等的数可以与它结合（可能原本有多余k个数，但是能和它合并一起消失的，只有k个）
        # 如...X DFD X DFDF X SDF [X LSKDFJ X LSJDFLK X DLKFJ...]
        # dp[i][j][k]表示只考虑[]部分对分数的贡献，那么[]中第一个X可能跟着前面K个X消失，也可能等着后面的X一起消失
        # 1. 跟前面的k个X一起消失的话，得分为(k+1)**2+helper(i+1,j,0)
        # 2.1 跟后面的第二个X一起消失的话，[]中的“LSKDFJ”部分独立拿分，X成为第二个X开头的子序的前导之一
        #     得分为helper(i+1,m-1,0)+helper(m,j,1+k)，m此时是[]中第二个X的序号
        #     这儿特别难理解，梳理一下过程，就是先消除“LSKDFJ”部分，得分为helper(i+1,m-1,0)
        #     然后再消除第二个X及向右的[]中部分，考虑到第二个X左侧有K+1个X，那么得分为helper(m,j,1+k)
        # 2.2 跟后面的第三个X一起消失的话，[]中的“LSKDFJ X LSJDFLK”部分独立拿分，X成为第三个X开头的子序的前导之一
        #     得分还是helper(i+1,m-1,0)+helper(m,j,1+k)，m此时是第三个X的序号
        # 2.3 至于“LSKDFJ”与“LSJDFLK”部分分别独立拿分，再合并k+3个X拿分的情况，包含于2.1情况中
        #     因为helper(m,j,1+k) 可以递归，下一层的2.1情况就是前K个与第一个X第二个X和第三个X合并
        #     所以只用考虑[]中第一个X与第Y个X直接合并，中间部分作为子区间独立拿分的情况
        # 几种情况取最高得分，并存入dp[i][j][k]
        
        def helper(i,j,k):
            if i > j:
                return 0
            if dp[i][j][k] != 0:
                return dp[i][j][k]
            # 大段连续的部分肯定是放一起消失得分高，而不是单个消失
            while i < j and boxes[i] == boxes[i+1]:
                i+=1
                k+=1
            res = (k+1)**2 + helper(i+1, j, 0)
            for m in range(i+1, j+1):
                if boxes[m] == boxes[i]:
                    res = max(res, helper(i+1, m-1, 0) + helper(m, j, 1+k))
                    
            dp[i][j][k] = res
            return dp[i][j][k]
        
        return helper(0,n-1,0)