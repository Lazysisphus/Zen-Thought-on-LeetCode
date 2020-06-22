class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        self.QuickSort(0, n - 1, nums)
        return nums

    # 快速排序
    # partition的两种写法
    def QuickSort(self, low, high, nums):
        if low < high:
            mid = self.partition2(low, high, nums)
            self.QuickSort(low, mid-1, nums)
            self.QuickSort(mid+1, high, nums)
    
    def partition1(self, low, high, nums):
        pivot = nums[high]
        i = low
        for j in range(low, high):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[high], nums[i] = nums[i], nums[high]
        return i

    def partition2(self, low, high, nums):
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