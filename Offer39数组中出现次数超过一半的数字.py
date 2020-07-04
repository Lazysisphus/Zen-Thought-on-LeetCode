class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法1：使用快速排序中的partition找到数组的中位数
        # 时间复杂度O(n)，但是无法通过
        def partition(low, high, nums):
            pivot = nums[low]
            while low < high:
                while low < high and nums[high] > pivot:
                    high -= 1
                nums[low] = nums[high] # low的值已经保存在pivot中
                while low < high and nums[low] < pivot:
                    low += 1
                nums[high] = nums[low]
            nums[low] = pivot
            return low
        
        if not nums:
            return None
        low, high = 0, len(nums)-1
        mid = low + (high - low) // 2
        pivot = partition(low, high, nums)
        while pivot != mid:
            if pivot < mid:
                low = mid + 1
                pivot = partition(low, high, nums)
            else:
                high = mid - 1
                pivot = partition(low, high, nums)
        return nums[mid]

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