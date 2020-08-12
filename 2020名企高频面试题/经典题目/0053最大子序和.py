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