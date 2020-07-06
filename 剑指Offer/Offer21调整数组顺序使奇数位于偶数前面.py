class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 方法1：双指针
        # 时间复杂度O(n)，空间复杂度O(1)
        if not nums:
            return []
        left = 0
        right = len(nums)-1
        while left <= right:
            if nums[left] % 2 == 1:
                left += 1
            elif nums[right] % 2 == 0:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums

        # 方法2：申请临时空间
        # 时间复杂度O(n)，空间复杂度O(n)
        num1=[]
        num2=[]
        for i in nums:
            if i % 2 != 0:
                num1.append(i)
            else:
                num2.append(i)
        return num1 + num2