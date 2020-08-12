class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 两次二分查找
        # 时间复杂度O(logn)
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        # 寻找左边界，即第一个target的索引
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        beg = left
        if nums[beg] != target:
            return [-1, -1]
        # 寻找右边界，即最后一个target的下一个数字的索引
        right = len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        end = left
        return [beg, end - 1]