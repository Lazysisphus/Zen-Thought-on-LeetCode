class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 这个思路无法很快想到，面试面出来我认输
        # 时间复杂度O(n)，空间复杂度O(1)
        n = len(nums)
        if n < 2:
            return nums
        # 从后向前，找到第一对升序对(i, j)(即满足前面的元素严格小于后面的元素)
        i = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0: # 如果不存在升序对，那么数组整体降序，返回数组的逆序(原地逆序)
            return nums.reverse()
        else:
            # 从[i, end]这个逆序范围寻找第一个大于nums[i - 1]的数字，和nums[i - 1]做交换
            j = n - 1
            while j >= i and nums[j] <= nums[i - 1]:
                    j -= 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
            for k in range((n - i) // 2): # [i, end]范围在交换后仍总体降序，现在进行逆序
                nums[i + k], nums[n - 1 - k] = nums[n - 1 - k], nums[i + k]