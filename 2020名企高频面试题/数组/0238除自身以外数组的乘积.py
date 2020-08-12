class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 时间复杂度O(n)，空间复杂度O(n)
        dp1 = [1 for _ in range(len(nums))]
        dp2 = [1 for _ in range(len(nums))]
        for i in range(1, len(dp1)):
            dp1[i] = dp1[i - 1] * nums[i - 1]

        for i in range(len(nums) - 1, 0, -1):
            dp2[i - 1] = dp2[i] * nums[i]

        for i in range(len(nums)):
            nums[i] = dp1[i] * dp2[i]
        return nums

        # 时间复杂度O(n)，空间复杂度O(1)
        ans = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]
        
        R = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = ans[i] * R
            R = R * nums[i]
        return ans