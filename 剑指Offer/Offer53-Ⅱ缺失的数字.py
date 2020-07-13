class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 二分查找
        # 时间复杂度O(logn)，空间复杂度O(1)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == mid: # 如果中间数字和下标相等，那么要找的缺失数字在后面
                left = mid + 1
            if nums[mid] != mid: # 如果中间数字和下标不等，那么分情况讨论
                if nums[mid-1] == mid-1: # 如果mid之前的数字与其下标相等，那么mid即为缺失的数字
                    return mid
                else:
                    right = mid - 1
        return left