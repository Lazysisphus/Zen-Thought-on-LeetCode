class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        self.QuickSort(0, n - 1, nums)
        return nums

    def SelectSort(nums):
        """
        选择排序
        时间复杂度O(n^2)
        不稳定，内排序
        """
        n = len(nums)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if nums[min_idx] > nums[j]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return nums

    def BubbleSort(nums):
        """
        冒泡排序
        时间复杂度O(n^2)
        稳定，内排序
        """
        n = len(nums)
        for i in range(n -1):
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    def InsertSort(nums):
        """
        插入排序
        时间复杂度O(n^2)
        稳定，内排序
        """
        n = len(nums)
        for i in range(1, n):
            for j in range(i, 0, -1):
                if nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
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