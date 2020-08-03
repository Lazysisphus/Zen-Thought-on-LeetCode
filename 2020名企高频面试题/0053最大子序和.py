'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp
        # dp[i]表示以nums[i]为最后数字的连续子串的最大和
        # 时间复杂度O(n)，空间复杂度O(n)
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)

        # dp
        # 优化空间复杂度为O(1)
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
        return max(nums)

        # 分治
        # 时间复杂度O(nlogn)，空间复杂度O(logn)(递归栈空间)
        if len(nums) == 1:
            return nums[0]
        
        mid = len(nums) // 2
        max_left = self.maxSubArray(nums[: mid])
        max_right = self.maxSubArray(nums[mid: ])
    
        max_l = nums[mid - 1]
        tmp = 0
        for i in range(mid - 1, -1, -1):
            tmp += nums[i]
            max_l = max(max_l, tmp)
        max_r = nums[mid]
        tmp = 0
        for i in range(mid, len(nums)):
            tmp += nums[i]
            max_r = max(max_r, tmp)
        return max(max_left, max_right, max_l+max_r)