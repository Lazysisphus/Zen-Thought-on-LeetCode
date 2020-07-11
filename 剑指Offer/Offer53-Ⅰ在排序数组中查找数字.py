class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 使用二分查找
        # 查找区间的右边界：
        #   如果 mid值 大于 target，那么 right = mid - 1
        #   如果 mid值 小于 target，那么 left = mid + 1
        #   如果 mid值 等于 target，右边界 end 在 mid 右侧，left = mid + 1
        #   退出循环时，left 指向第一个大于 target 的元素，right “应该”指向最末尾的target
        # 时间复杂度O(logn)，空间复杂度O(1)
        if not nums:
            return 0
        
        # 搜索最末 target
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
            end = left
        end = left
        # 若数组中无 target ，则提前返回
        if right >= 0 and nums[right] != target: 
            return 0

        # 搜索最初 target
        left = 0
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target: 
                left = mid + 1
            else: 
                right = mid - 1
        start = right
        return end - start - 1