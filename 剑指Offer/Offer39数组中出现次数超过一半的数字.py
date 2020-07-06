class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法1：使用快速排序中的partition找到数组的中位数
        # 时间复杂度O(n)，但是无法通过
        def partition(nums, low, high):
            pivot = nums[low]
            while low < high:
                while low < high and nums[high] >= pivot:
                    high -= 1
                nums[low] = nums[high] # low的值已经保存在pivot中
                while low < high and nums[low] <= pivot:
                    low += 1
                nums[high] = nums[low]
            nums[low] = pivot
            return low
        
        if not nums:
            return None
        low, high = 0, len(nums)-1
        mid = low + (high - low) // 2
        index = partition(nums, low, high)
        while index != mid:
            if index > mid:
                high = index - 1
                index = partition(nums, low, high)
            else:
                low = index + 1
                index = partition(nums, low, high)
        return nums[index]

        # 方法2：摩尔投票法
        # 时间复杂度O(n)
        if not nums:
            return None
        
        ans = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if cnt == 0:
                ans = nums[i]
                cnt = 1
            elif nums[i] == ans:
                cnt += 1
            else:
                cnt -= 1
        return ans