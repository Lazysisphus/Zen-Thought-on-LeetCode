class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 双指针
        # 时间复杂度O(n)，空间复杂度O(1)
        left = 0
        right = len(nums) - 1
        while left < right:
            tmp = nums[left] + nums[right]
            if tmp == target:
                return [nums[left], nums[right]]
            elif tmp < target:
                left += 1
            else:
                right -= 1
        return []